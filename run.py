# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
"""This weather guessing game with random locations"""
print("Welcome to the WeaterGuesser!")


def validate_username(username):
    if not username.isalpha():
        return False
    if len(username) < 3 or len(username) > 16:
        return False
    return True


username = input("Enter your username (4-16 alphabetical characters): ")


# Validate the username
if validate_username(username):
    print("Hello, " + username + "! "
          "Welcome again to the WeatherGuesser. "
          "Following you will guess the weather in a "
          "random location from all over the world!")
else:
    print("Username should contain 4 to 16 alphabetical characters only.")
