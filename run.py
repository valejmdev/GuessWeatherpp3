# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
"""This weather guessing game with random locations"""
# Import for required libaries
import requests
import pandas as pd
import random

# OpenWeather.org API Key for Realtime Information
api_key = "b092090963bc7750c270ab36f9bc42e9"

# Base url for the OpenWeather API
root_url = "http://api.openweathermap.org/data/2.5/weather?"

# Welcome Message
print("Welcome to the WeaterGuesser!")


def get_random_city():
    df = pd.read_csv("cities.csv")
    city_column = "City"
    random_city = random.choice(df[city_column].tolist())
    return random_city


# Validation Rules for the username
def validate_username(username):
    if not username.isalpha():
        return False
    if len(username) < 3 or len(username) > 16:
        return False
    return True


# Validating the username
while True:
    username = input("Enter your username (3-16 alphabetical characters): ")

    if validate_username(username):
        print("Hello, " + username + "! "
              "Welcome again to the WeatherGuesser. "
              "Following you will guess the weather in a "
              "random location from all over the world!")
        break
    else:
        print("Username should contain 3 to 16 alphabetical characters only.")

def api_call():
    # City name input for testing
    city_name = get_random_city()

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
        
        return weather_condition, temperature_range, city_name
    
    else:
        print("Something went wrong... Please try again...")
        return None, None, None

    

weather_condition, temperature_range, city_name = api_call()

# Class for questions
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

if city_name and weather_condition and temperature_range:
    # Array for questions
    weather_prompt = [
        "How is the weather for the day in:" + city_name +
        "\n(1) Sunny\n(2) Cloudy\n(3) Overcast\n(4) Rain/Snow\n(5) Thunderstorm",
        "How warm is it for the day in:" + city_name +
        "\n(1)less than 0°C\n(2) 0-10°C\n(2) 10°C-20°C\n(3) 20°C-30°C\n"
        "(5) more than 30°C\n"
        ]

    # Correct answer validation
    questions_validation = [
        Question(weather_prompt[0], weather_condition),
        Question(weather_prompt[1], temperature_range)
    ]


    # Validation for the answer given by the user
    def guess_validation(prompt):
        while True:
            user_input = input(prompt)
            if user_input.isdigit() and user_input in ("1", "2", "3", "4", "5"):
                return user_input
            else:
                print("Please enter a number from 1-5")


    # Function of the guesser game
    def run_guesser(questions_validation):
        score = 0
        for i, question in enumerate(questions_validation, 1):
            user_answer = input(f"Question {i}: {question.question}"
                                "\nEnter your answer: ")
            if user_answer == str(question.answer):
                score += 1
        print("You got " + str(score) + '/' + str(len(questions_validation)) +
            " correct")


    # Calling guesser game function
    run_guesser(questions_validation)
else:
    print("Could not retrieve weather data. Exiting the game.")