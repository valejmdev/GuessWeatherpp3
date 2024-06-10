# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
"""This weather guessing game with random locations"""
# Import for required libaries
import requests
import random
import time
from colorama import Fore, Style, init
init(autoreset=True)
import gspread
from google.oauth2.service_account import Credentials

init()

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_Client = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_Client.open('guessweatherpp3')

CITIES_LIST = SHEET.worksheet('cities_list')
LEADERBOARD = SHEET.worksheet('leaderboard')

# OpenWeather.org API Key for Realtime Information
api_key = "b092090963bc7750c270ab36f9bc42e9"

# Base url for the OpenWeather API
root_url = "http://api.openweathermap.org/data/2.5/weather?"


def get_random_city_and_country():
    data = CITIES_LIST.get_all_values()

    headers = data[0]
    rows = data[1:]
    cities = [dict(zip(headers, row)) for row in rows]
    
    random_city_info = random.choice(cities)
    random_city = random_city_info['City']
    random_country = random_city_info['Country']
    
    return random_city, random_country


# Validation Rules for the username
def validate_username(username):
    if not username.isalpha():
        return False
    if len(username) < 3 or len(username) > 16:
        return False
    return True


# Validating the username
def start_guesser():
    # Welcome Message
    print("Welcome to the WeaterGuesser!")
    while True:
        username = input("Enter your username (3-16 alphabetical characters): \n")

        if validate_username(username):
            print("Hello, " + username + "! "
                "Welcome again to the WeatherGuesser. "
                "Following you will guess the weather in a "
                "random location from all over the world!")
            return username
        else:
            print(Fore.RED + "The username should contain 3 to 16 alphabetical characters only." + Style.RESET_ALL)


def api_call():
    # City name input for testing
    city_name, country_name = get_random_city_and_country()
    if city_name is None or country_name is None:
        return None, None, None, None
    
    # Building url for testing api call
    url = f"{root_url}appid={api_key}&q={city_name}"

    # Sending a get request at the url
    r = requests.get(url)

    # Saving the data returned by the API
    data = r.json()

    # Checking if there is no error and the status code is 200
    if data['cod'] == 200:
        # Getting the raw temperature in Kelvin form the json data
        temp_kelvin = data['main']['temp']
        # Converting temperatur from Kelvin to Celsius
        temp_celcius = temp_kelvin - 273.15

        # Getting the description of the weather from the json data
        descr = data['weather'][0]['description']

        if "clear sky" in descr:
            weather_condition = "1"
        elif "few clouds" in descr or "scattered clouds" in descr:
            weather_condition = "2"
        elif "broken" in descr or "shower rain" in descr:
            weather_condition = "3"
        elif "rain" in descr or "snow" in descr:
            weather_condition = "4"
        else:
            weather_condition = "5"

        if temp_celcius < 0:
            temperature_range = "1"
        elif temp_celcius < 10:
            temperature_range = "2"
        elif temp_celcius < 20:
            temperature_range = "3"
        elif temp_celcius < 30:
            temperature_range = "4"
        else:
            temperature_range = "5"
        
        return weather_condition, temperature_range, city_name, country_name
    
    else:
        print(Fore.RED + "Something went wrong... Please try again..." + Style.RESET_ALL)
        return None, None, None


# Class for questions
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


def question_creator(city_name, country_name, weather_condition, temperature_range):
        # Array for questions
        weather_prompt = [
            "How is the weather for the day in: " + city_name +", " + country_name +
            "\n(1) Sunny\n(2) Cloudy\n(3) Overcast\n(4) Rain/Snow\n(5) Thunderstorm",
            "How warm is it for the day in: " + city_name +", " + country_name +
            "\n(1)less than 0°C\n(2) 0-10°C\n(3) 10°C-20°C\n(4) 20°C-30°C\n"
            "(5) more than 30°C\n"
            ]
        

        # Correct answer validation
        questions_validation = [
            Question(weather_prompt[0], weather_condition),
            Question(weather_prompt[1], temperature_range)
        ]

        return questions_validation


# Validation for the answer given by the user
def guess_input_validation(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and user_input in ("1", "2", "3", "4", "5"):
            return user_input
        else:
            print(Fore.RED + "Please enter a number from 1-5" + Style.RESET_ALL)


    # Function of the guesser game
def run_guesser(questions_validation):
    score = 0
    for i, question in enumerate(questions_validation, 1):
        user_answer = guess_input_validation(f"Question {i}: {question.question}\nEnter your answer: \n")
        if user_answer == str(question.answer):
            score += 1
    print(Fore.GREEN +"You got " + str(score) + '/' + str(len(questions_validation)) + " correct" + Style.RESET_ALL)
    return score 


def update_leaderboard(username, score):
    records = LEADERBOARD.get_all_records()
    for record in records:
        if record['Username'] == username:
            if score > int(record['Highscore']):
                record['Highscore'] = score
                LEADERBOARD.update_cell(records.index(record) + 2, 2, score)
            return
    LEADERBOARD.append_row([username, score])


def loading_animation(duration):
    for _ in range(duration * 10):  
        print("Loading", end="")
        for _ in range(3):  
            print(".", end="")
            time.sleep(0.1)  
        print("\r", end="") 


def end_game():
    while True:
                print("\nWhat would you like to do next?")
                print("1. Reset game")
                print("2. Exit")
                choice = input("Enter your choice (1 or 2):\n")
                
                if choice == "1":
                    # Reset the game by re-running the main function
                    print("Resetting game...")
                    main()
                    return
                elif choice == "2":
                    # Exit the game
                    print("Exiting the game. Goodbye!")
                    return
                else:
                    print(Fore.RED + "Invalid choice. Please enter 1 or 2." + Style.RESET_ALL)


# Calling guesser game function
def main():
    username = start_guesser()
    total_score = 0
    rounds = 3
    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number}/{rounds}")
        weather_condition, temperature_range, city_name, country_name = api_call()
        print(Fore.YELLOW + "Please wait... Gathering data." + Style.RESET_ALL)
        loading_animation(2)
        if city_name and weather_condition and temperature_range:
            questions_validation = question_creator(city_name, country_name, weather_condition, temperature_range)
            round_score = run_guesser(questions_validation)
            if round_score is not None: 
                total_score += round_score
        else:
            print(Fore.RED + "Could not retrieve weather data for this round." + Style.RESET_ALL)
    
    print(Fore.GREEN + f"\nGame Over! {username}, your total score is: {total_score}/{rounds * 2}" + Style.RESET_ALL)
    update_leaderboard(username, total_score)
    end_game()

# Run the main function
if __name__ == "__main__":
    main()