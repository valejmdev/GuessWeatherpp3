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
        print("Username should contain 3 to 16 alphabetical characters only. Please try again.")

        
