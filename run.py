"""This weather guessing game with random locations"""
# Import for required libaries
import requests
import random
import time
import os
import json
from colorama import Fore, Style, init
import gspread
from google.oauth2.service_account import Credentials

# Colorma Setting
init(autoreset=True)

# Credentials import
with open('creds.json') as f:
    creds_data = json.load(f)

# Google Drive import
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Getting Information from Google Spreadsheet
CREDS = Credentials.from_service_account_info(creds_data['gspread'])
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_Client = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_Client.open('guessweatherpp3')

# Getting Information from different Lists in Google Spreadsheet
CITIES_LIST = SHEET.worksheet('cities_list')
LEADERBOARD = SHEET.worksheet('leaderboard')
leaderboard_values = LEADERBOARD.get_all_values()
headers = leaderboard_values[0]
leaderboard_data = [dict(zip(headers, row)) for row in leaderboard_values[1:]]
SORTED_LEADERBOARD = sorted(leaderboard_data, key=lambda x: x['Highscore'],
                            reverse=True)


# Base url for the OpenWeather API
ROOT_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = creds_data['openweather']['API_KEY']

# Help String that shows Tutorial
HELP_STRING = """
In this game, you will guess the weather conditions and temperature ranges
\nfor random cities around the world. Here’s how you play:

1. **Game Rounds**:
    - The game consists of 3 rounds.
    - In each round, you will be presented with a random city and country.

2. **Guess the Weather**:
    - For each city, you will answer two questions:
     1. **Weather Condition**:
     2. **Temperature Range**:

3. **Enter Your Answers**:
    - Type a number from 1 to 5 corresponding to your guess and press Enter.
    - If you need to read these rules again, type 'help' and press Enter.

4. **Feedback**:
    - Correct answers will be highlighted in green.
    - Incorrect answers will be highlighted in red, and the correct answer
      will be shown.

5. **End of Game**:
    - After all rounds are completed, your total score will be displayed.
    - Your score will be recorded on the leaderboard.

Enjoy the WeatherGuesser Game and have fun guessing the weather around
the world!\n
------------------------------------------------------------------------\n
"""


def get_random_city_and_country():
    """
    Function to get a city with it's corresponding country, from the
    google spreasheet cities list by converting it into a dictionary.
    The city is chosen randomly with the python random method.
    """

    data = CITIES_LIST.get_all_values()

    headers = data[0]
    rows = data[1:]
    cities = [dict(zip(headers, row)) for row in rows]
    random_city_info = random.choice(cities)
    random_city = random_city_info['City']
    random_country = random_city_info['Country']
    return random_city, random_country


def validate_username(username):
    """
    Function to create validation rules for the username, so
    that the user can only use alphabetical characters,
    not less than 3 and not more than 16 characters.
    """
    if not username.isalpha():
        return False
    if len(username) < 3 or len(username) > 16:
        return False
    return True


def start_guesser():
    """
    This is a function that greets the user and instructs him with a simple
    tutorial. After pressing the "Enter" key the user is asked to enter
    an username, that meets the validation rules above.
    """
    # Welcome Message
    print("Welcome to the WeatherGuesser!")
    print(HELP_STRING)
    input("Press 'Enter' to continue")
    clear()
    while True:
        username = input("Enter your username " +
                         "(3-16 alphabetical characters): \n")

        if validate_username(username):
            return username
        else:
            print(Fore.RED + "The username should contain 3 to 16" +
                  " alphabetical characters only." + Style.RESET_ALL)


def api_call():
    """
    This function sends the randomly chosen city to the
    OpenWeather API. Then the function takes the current weather
    conditon and current temperature of that city and
    summarizes it to a value that can be guessed more easily.
    If there is a issue with any of the requests or information,
    the user will be informed, that an error has occured, but
    the game will still run.
    """
    # City name input for testing
    city_name, country_name = get_random_city_and_country()
    if city_name is None or country_name is None:
        return None, None, None, None

    # Building url for testing api call
    url = f"{ROOT_URL}appid={API_KEY}&q={city_name}"

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
        # print statement in case of any request error
        print(Fore.RED + "Something went wrong... Please try again..." +
              Style.RESET_ALL)
        return None, None, None


# Class for questions
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


def question_creator(city_name, country_name, weather_condition,
                     temperature_range):
    """
    This function takes the random city and its corresponding
    country, to include them in the question. It also shows
    the user the possible guess values and how to guess them.
    It creates two rounds, in the first you are asked for the
    weather condition and the secont for the temperature.
    """
    # Array for questions
    weather_prompt = [
        Fore.LIGHTWHITE_EX + "How is the weather for the day in: " +
        city_name + "," + country_name + Style.RESET_ALL +
        "\n(1) Sunny\n(2) Cloudy\n(3) Overcast\n(4) Rain/Snow " +
        "\n(5) Thunderstorm",
        Fore.LIGHTWHITE_EX + "How warm is it for the day in: "
        + city_name + ", " + country_name + Style.RESET_ALL +
        "\n(1)less than 0°C\n(2) 0-10°C\n(3) 10°C-20°C\n(4) 20°C-30°C\n"
        "(5) more than 30°C\n"
        ]
    # Correct answer validation
    questions_validation = [
        Question(weather_prompt[0], weather_condition),
        Question(weather_prompt[1], temperature_range)
    ]

    return questions_validation


def guess_input_validation(prompt):
    """
    This function creates the validation rules for the input
    of the user in the guesser game part. Here the users is limited
    to the usage of the numbers 1-5 and the word 'help'.
    If the input is 'help' the user will see the Tutorial Text from
    the beginning again and can still play the round.
    """
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and user_input in ("1", "2", "3", "4", "5"):
            return user_input
        elif user_input.isalpha() and user_input == ("help"):
            clear()
            print(HELP_STRING)
        else:
            print(Fore.RED + "Please enter a number from 1-5\n"
                  + Style.RESET_ALL)


def run_guesser(questions_validation):
    """
    This function creates the gameloop combining the questions and
    corresponding answers with the input validation. It creates
    multiple rounds, so that more than one question can be displayed.
    With a input that meets the validation rules above, the user
    gets an direct and visual feedback to their guess, even showing
    the right answer, when guessed wrong.
    """
    score = 0
    for i, question in enumerate(questions_validation, 1):
        my_color = Fore.WHITE
        user_answer = guess_input_validation(
            Fore.LIGHTWHITE_EX + f"Question {i}: {my_color}{question.question}"
            "\nEnter your answer: \n")
        if user_answer == str(question.answer):
            print(Fore.GREEN + "Correct!\n" + Style.RESET_ALL)
            print("---------------------------------------------------------")
            score += 1
        else:
            print(Fore.RED +
                  f"Wrong! The correct answer was {question.answer}." +
                  Style.RESET_ALL)
            print("---------------------------------------------------------")
    print(Fore.GREEN + "You got " + str(score) + '/' +
          str(len(questions_validation)) + " correct" + Style.RESET_ALL)
    return score


def update_leaderboard(username, score):
    """
    This function updates the users username and total score to
    the leaderboard. It also checks if the username is already
    existing in the leaderboard. If that is the case the score
    only gets updated, when the total score is higher than the
    recorded one.
    """
    records = LEADERBOARD.get_all_records()
    for record in records:
        if record['Username'] == username:
            if score > int(record['Highscore']):
                record['Highscore'] = score
                LEADERBOARD.update_cell(records.index(record) + 2, 2, score)
            return
    LEADERBOARD.append_row([username, score])


def show_leaderboard():
    """
    This function displays the leaderboard of the google
    spreadsheet. It not only formats it to please the eye,
    but also sorts it for the highest score to the lowest.
    It always takes the updated information as soon as it is
    called.
    """
    leaderboard_values = LEADERBOARD.get_all_values()
    headers = leaderboard_values[0]
    leaderboard_data = [dict(zip(headers, row
                                 )) for row in leaderboard_values[1:]]
    sorted_leaderboard = sorted(leaderboard_data, key=lambda x:
                                (int(x['Highscore']), x[
                                 'Username']), reverse=True)

    print(Fore.YELLOW + "\nLeaderboard:\n" + Style.RESET_ALL)
    print(f"{'Username':<16}{'Highscore':<5}")
    print('-' * 21)
    for record in sorted_leaderboard:
        print(f"{record['Username']:<16}{record['Highscore']:<5}")


# Function for visual Loading animation to prevent API errors
def loading_animation(duration):
    """
    This function creates a visual Loading animation to
    give the API requests enough time to take the random
    city and respond with the current weather information.
    It also creates suspense and gives a interactive notion
    to the application.
    """
    for _ in range(duration * 10):
        print("Loading", end="")
        for _ in range(3):
            print(".", end="")
            time.sleep(0.1)
        print("\r", end="")


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


# Function to give user the
def end_game():
    """
    This function gives the user the option to input 1-3 to
    either reset the game to start new, show the leaderboard or exit
    the game, which closes the application.
    """
    while True:
        print("\nWhat would you like to do next?")
        print("1. Reset game")
        print("2. Show Leaderboard")
        print("3. Exit")
        choice = input("Enter your choice (1, 2 or 3):\n")
        if choice == "1":
            # Reset the game by re-running the main function
            print("Resetting game...")
            main()
            return
        elif choice == "2":
            clear()
            print("The Leaderboard...")
            show_leaderboard()
        elif choice == "3":
            # Exit the game
            print("Exiting the game. Goodbye!")
            return
        else:
            print(Fore.RED + "Invalid choice. Please enter 1 or 2." +
                  Style.RESET_ALL)


# Calling guesser game function and creating the game loop
def main():
    """
    This is the main function that uses all the functions
    created above in a logic order. It also creates a loop
    that let's the user guess for 3 different cities.
    It has an error handling message and is called at the end
    of my python file.
    """
    username = start_guesser()
    total_score = 0
    rounds = 3
    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number}/{rounds}")
        (
         weather_condition,
         temperature_range,
         city_name,
         country_name,
        ) = api_call()
        print(Fore.YELLOW + "Please wait... Gathering data." + Style.RESET_ALL)
        loading_animation(2)
        if city_name and weather_condition and temperature_range:
            questions_validation = question_creator(
                city_name, country_name, weather_condition, temperature_range)
            round_score = run_guesser(questions_validation)
            if round_score is not None:
                total_score += round_score
        else:
            print(Fore.RED +
                  "Could not retrieve weather data for this round." +
                  Style.RESET_ALL)
    print(
          Fore.GREEN +
          f"\nGame Over! {username}, your total score is: {total_score}/"
          f"{rounds * 2}" +
          Style.RESET_ALL
         )
    update_leaderboard(username, total_score)
    end_game()


# Run the main function
if __name__ == "__main__":
    main()
