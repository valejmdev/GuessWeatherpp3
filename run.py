# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
"""This weather guessing game with random locations"""
# Import for required libaries
import requests

# OpenWeather.org API Key for Realtime Information
api_key = "b092090963bc7750c270ab36f9bc42e9"

# Base url for the OpenWeather API
root_url = "http://api.openweathermap.org/data/2.5/weather?"

# Welcome Message
print("Welcome to the WeaterGuesser!")


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


# City name input for testing
city_name = input("What city do you want to guess for? ")

# Building url for testing api call
url = f"{root_url}appid={api_key}&q={city_name}"

# Sending a get request at the url
r = requests.get(url)

# Displaying the json weather data returned by the api
print(r.json())

data = r.json()

# Checking if there is no error and the status code is 200
if data['cod'] == 200:
    # Getting the temperature form the json data
    temp = data['main']['temp']
    # Getting the description of the weather from the json data
    descr = data['weather'][0]['description']

    print(f"City Name: {city_name}")
    print(f"Weather Condition is {descr}")
    print(f"The temperatur is: {temp}")

else:
    print("Something went wrong... Please try again...")


# Class for questions
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


# Array for questions
weather_prompt = [
    "How is the weather for the day in:" + city_name +
    "\n(1) Sunny\n(2) Mostly Sunny\n(3) Mostly Cloudy\n(4) Overcast\n",
    "How warm is it for the day in:" + city_name +
    "\n(1) less than 10°C\n(2) 10°C-20°C\n(3) 20°C-30°C\n(4) more than 30°C\n"
    ]

# Correct answer validation
questions_validation = [
    Question(weather_prompt[0], "2"),
    Question(weather_prompt[1], "3")
]


# Function of the guesser game
def run_guesser(questions_validation):
    score = 0
    for question in questions_validation:
        answer = input(question.question)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + '/' + str(len(questions_validation)) +
          " correct")


# Calling guesser game function
run_guesser(questions_validation)
