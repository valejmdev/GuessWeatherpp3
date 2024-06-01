# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
"""This weather guessing game with random locations"""
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

current_city = "Zwickau"


class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


weather_prompt = [
    "How is the weather for the day in:" + current_city +
    "\n(1) Sunny\n(2) Mostly Sunny\n(3) Mostly Cloudy\n(4) Overcast\n",
    "How warm is it for the day in:" + current_city +
    "\n(1) less than 10°C\n(2) 10°C-20°C\n(3) 20°C-30°C\n(4) more than 30°C\n"
    ]


questions_validation = [
    Question(weather_prompt[0], "2"),
    Question(weather_prompt[1], "3")
]


def run_guesser(questions_validation):
    score = 0
    for question in questions_validation:
        answer = input(question.question)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + '/' + str(len(questions_validation)) +
          " correct")


run_guesser(questions_validation)
