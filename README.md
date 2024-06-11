
# The Weather Guesser


## Introduction

Welcome to **The Weather Guesser**, an engaging and interactive game where you can test your weather prediction skills! This application invites you to enter a username and guess the weather in various cities around the world. It's a fun way to learn about global weather patterns and challenge yourself to see how well you can predict the weather conditions and temperatures in different locations.

This project was created as part of Code Institute's Full Stack Software Development Diploma, demonstrating a comprehensive integration of Python, the OpenWeather API, Google Sheets API, and web development techniques.



## The Weather Guesser
# Screenshot
![I Am Responsive]()
### View the live website [here](https://guessweatherpp3-45effae546b9.herokuapp.com)
***
## Table of content: 
## Contents

* [User Experience](#user-experience)
   * [User Benefits](#user-benefits)
   * [User Stories](#user-stories)
   * [Program Flowchart](#program-flowchart)
* [Technologies Used](#technologies-used)
* [Data Storage](#data-storage-google-sheets)
* [Features](#features)
   * [Username Validation](#username-validation)
   * [Weather Data Fetching](#weather-data-fetching)
   * [Interactive Gameplay](#interactive-gamepla)
   * [Scoring System](#scoring-system)
   * [Leaderboard](#leaderboard)
   * [Game Options](#game-options)
   * [User Feedback](#user-feedback)
   * [Loading Animation](#loading-animation)
* [Python Packages Used](#python-packages-used)
* [Testing](#testing)
   * [Python PEP8 Validation](#python-pep8-validation)
   * [Development Bugs](#development-bugs)
* [Deployment and Development](#deployment-and-development)
   * [Deploying the App](#deploying-the-app)
   * [Forking The Repository](#forking-the-repository)
   * [Cloning The Repository](#cloning-the-repository)
   * [APIs](#apis)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)
***
## User Experience: 

### User Stories: 
#### Persona:
##### Demographics

-   **Name:** Alex Johnson
-   **Age:** 28
-   **Occupation:** Software Developer
-   **Location:** Seattle, WA

##### Background

Alex is a tech-savvy software developer who enjoys coding, gaming, and solving puzzles. He loves participating in quizzes and trivia games, and is always on the lookout for new and entertaining activities to unwind after work.

##### Motivations and Goals

-   **Intellectual Challenge:** Alex enjoys testing his knowledge and problem-solving skills.
-   **Learning:** He seeks to expand his knowledge about different places and their weather patterns.
-   **Entertainment:** He looks for engaging activities to break from his routine.
-   **Competition:** Alex likes to compare his performance with others through leaderboards.

##### How Alex Uses the Weather Guesser App

-   **During Breaks:** Plays the game to relax and recharge.
-   **Learning:** Uses the app to learn about global weather conditions.
-   **Competing:** Challenges friends and checks the leaderboard to see his ranking.
-   **Improving Knowledge:** Appreciates the feedback after each round to learn from mistakes.

##### Why Alex Loves the Weather Guesser App

-   **Engaging and Challenging:** Provides an exciting way to test his weather knowledge.
-   **Educational:** Offers a fun way to learn about different climates.
-   **Competitive Leaderboard:** Fuels his competitive spirit and motivates improvement.
-   **User-Friendly:** Intuitive interface and smooth user experience.

***
##### Detailed User Journey

##### Phase 1: Discovery

1.  **Trigger:** Alex learns about the app from a tech blog and gets intrigued.
2.  **Research:** Visits the website, reads reviews, and watches a demo video.
3.  **Decision:** Decides to download and try the app.

##### Phase 2: Onboarding

1.  **Account Creation:** Downloads the app, creates a username "AlexJ".
2.  **Tutorial:** Receives a brief tutorial on how to play the game.

##### Phase 3: Gameplay

1.  **Starting a Game:** Begins his first game session with a random city.
2.  **Question Interaction:** Inputs his weather guess, receives instant feedback.
3.  **Score Tracking:** Sees his score update in real-time after each round.
4.  **End of Round:** Views his total score and updates the leaderboard.

##### Phase 4: Leaderboard and Social Interaction

1.  **Viewing the Leaderboard:** Checks his ranking against other players.
2.  **Challenge Friends:** Competes with friends to improve his rank.

##### Phase 5: Retention and Advocacy

1.  **Loyal User:** Becomes a regular player, finding the app fun and educational.
2.  **Advocate:** Recommends the app to colleagues and friends, writes positive reviews.


***
### User Benefits

-   **Engaging Entertainment:**
    
    -   Enjoy a fun and interactive game that tests your weather knowledge.
    -   Experience the excitement of guessing weather conditions in various global cities.
  
-   **Educational Value:**
    
    -   Learn about different cities and their weather patterns while playing.
    -   Improve your geographical and meteorological knowledge in an enjoyable way.

-   **Social Interaction:**
    
    -   Compete with friends and other users on the global leaderboard.

-   **Real-time Information:**
    
    -   Access accurate and up-to-date weather information for cities worldwide.
    -   Stay informed about weather conditions while enjoying the game.

-   **User-friendly Experience:**
    
    -   Enjoy a smooth and intuitive interface designed for ease of use.
    -   Quickly get started with clear instructions and helpful prompts.

-   **Motivation and Rewards:**
    
    -   Receive instant feedback and scores to keep you motivated.
    -   Strive for high scores and climb the leaderboard for recognition.

-   **Accessibility:**
    
    -   Play on various devices, including smartphones, tablets, and computers.
    -   Easily access the game anytime, anywhere for quick entertainment.


### Program Flowchart
# Screenshot
![Programm Flowchart]()

## Technologies Used: 
-   **Python:** For backend logic and API interactions.
-   **Google Sheets API:** For storing and displaying the leaderboard.
-   **Colorama:** For color-coded terminal outputs.
-   **gspread:** For interacting with Google Sheets.
 -   **OpenWeather API:** [To fetch real-time weather data.]()
-   **Heroku:** [For deploying the application.]()
-	**Whimsical:** [For creating the program flowchart.]()
-	 **StackEdit** [For creating the README.md.](https://stackedit.io/)
***
## Features: 
# Screenshot
-   **Tutorial Introduction:**
    -   Greets the user and gives him a brief tutorial how to play the game.
# Screenshot
-   **Username Validation:**
    -   Ensures the entered username is between 3 to 16 alphabetical characters.
# Screenshot
-   **Weather Data Fetching:**
    -   Uses OpenWeather API to fetch real-time weather data for random cities.
# Screenshot
-   **Question Generation:**
    -   Creates weather-related questions based on the fetched data.
# Screenshot
-   **Interactive Gameplay:**
    -   Users answer questions about the weather, scoring points for correct answers.
    -   Feedback is provided on the correctness of each answer, with correct answers highlighted in green and 		incorrect ones in red.
# Screenshot
-   **Scoring System:**
    -   Tracks and updates the total score across multiple rounds.
# Screenshot
-   **Leaderboard:**
    -   Stores and displays high scores, sorted by score and alphabetically by username for ties.
    -   Provides real-time updates to the leaderboard after each game.
# Screenshot
-   **Game Options:**
    -   Allows users to reset the game, view the leaderboard, or exit the game after completing the rounds.
# Screenshot
-   **User Feedback:**
    -   Uses color-coded messages (via Colorama) to enhance user experience.
# Screenshot
-   **Loading Animation:**
    -   Displays a loading animation while fetching weather data to enhance user engagement.

## Python Packages Used
The Weather Guesser application relies on the following Python packages for its functionality:

-   **requests:** Used for making HTTP requests to fetch weather data from the OpenWeather API.
    
-   **random:** Utilized for generating random elements, such as selecting a random city for the game.
    
-   **time:** Used for adding delays, such as simulating a loading animation or waiting for API responses.
    
-   **os:** Enables interaction with the operating system, facilitating tasks like file operations.
    
-   **json:** Used for parsing JSON data returned from API requests.
    
-   **colorama:** Provides support for colored terminal text, enhancing the visual presentation of the application.
    
-   **gspread:** Allows interaction with Google Sheets, used for storing and updating the leaderboard data.
    
-   **google.oauth2.service_account:** Required for authenticating access to Google Sheets using a service account.

These packages, along with their respective versions, are listed in the `requirements.txt` file for easy installation using pip.


## Data Storage
The Weather Guesser app employs Google Sheets for effective data storage and management. Here’s how the data is organized and utilized within the app:
# Screenshot
1.  **City and Country List:**
    -   A worksheet named `cities_list` contains a comprehensive list of cities along with their respective countries. This data is essential for randomly selecting a city for each game round, ensuring a diverse and engaging user experience.
# Screenshot
2.  **Leaderboard:**
    -   Usernames and their corresponding high scores are stored in a worksheet named `leaderboard`. This feature tracks each player’s highest score, allowing the app to display a dynamic and up-to-date leaderboard showcasing the top performers.

### Data Handling and Privacy

1.  **Google Sheets Integration:**
    -   The app integrates with Google Sheets using the `gspread` library. Authentication is handled via a service account, with credentials securely stored in a `creds.json` file. This file is kept out of the repository to maintain security.

2.  **Data Privacy:**
    -   All credentials, including the service account and API keys, are kept secure and private. This approach ensures that user data is protected and the application’s integrity is maintained.

3.  **Real-Time Updates:**
    -   The leaderboard is updated in real-time, allowing users to see the latest high scores immediately after each game round. This feature enhances the competitive aspect of the game.

4.  **Security Measures:**
    
    -   Access to the Google Sheets API is managed through OAuth2, with restricted scopes to limit access to only necessary operations. This enhances the security of data interactions within the app.


## Testing
I conducted extensive manual testing of the Weather Guesser application to ensure its functionality and reliability. Here's an overview of the testing process and outcomes:

-   **Manual Testing:** I personally tested the application multiple times on different devices and browsers to verify its performance and responsiveness.
    
-   **Peer Review:** I shared the application with peers, friends, and family members, requesting their feedback and insights. They tested various features and provided valuable input on usability and functionality.
    
-   **API Error Handling:** The application was rigorously tested to handle API requests gracefully, including scenarios where there were timeouts or errors in fetching data. The app responded appropriately without crashing or disrupting the user experience.
    

Overall, the testing results were highly satisfactory, with the application running smoothly and as intended in all tested scenarios. Any detected issues were promptly addressed, ensuring a seamless user experience for all players.

### Python PEP8 Validation
During the development in VS Code i used the autopep8 and Flake8 Extensions. Due to a issue up on starting the workspace i had to disable it until the end of the development phase and re-enable it for validation later on.
I also validated the Code via the CI Python Linter
https://pep8ci.herokuapp.com/#

# Screenshot

## Development Bugs

| Bug Description                                            | Status |
|-----------------------------------------------------------|--------|
| Username displayed as None at the end of the game         | &#10003; |
| Leaderboard not updated in real-time                       | &#10003; |
| Used different list of cities before, which gave 404 error | &#10003; |
| Load animation for timeout error of API                    | &#10003; |
| Removed pandas because Heroku can't parse it sometimes     | &#10003; |
| Changed from CSV to Google Spreadsheet                     | &#10003; |
| Tried OpenWeatherMap 3.0 OneCall API, but was asked for a subscription, so i used 2.5 API from  the YouTube tutorial mentioned below| &#10003; |
| Had to convert spreadsheet into dict to sort the leaderboard | &#10003; |
| Leaderboard update didn't work in round, only after closing and rerunning game I get the update shown | &#10003; |

## Deployment
The Guess Weather App was developed using Gitpod for code creation and file management. The project files, code, and related information are hosted on GitHub
### Deploying the App

To deploy the Guess Weather App on Heroku, follow these steps:

1.  **Heroku Account Setup:** Log in to Heroku or create an account if you haven't already.
2.  **Create a New App:** From the Heroku dashboard, click on the "New" button and select "Create new app" from the dropdown menu.
3.  **App Configuration:** Provide a unique name for your application and select the appropriate region.
    -   Example: Name: "guess-weather-app", Region: Europe.
4.  **Add Config Vars (if necessary):**
    -   If your project uses a `creds.json` file, add a config var:
        -   Key: `CREDS`
        -   Value: Contents of your `creds.json` file.
5.  **Set Buildpacks:**
    -   Navigate to the "Settings" tab and locate the "Buildpacks" section.
    -   Click on "Add buildpack" and select Python.
    -   Add another buildpack for Node.js.
    -   Ensure that the Python buildpack is positioned above the Node.js buildpack.
6.  **Deploy from GitHub:**
    -   Go to the "Deploy" section and choose "GitHub" as the deployment method.
    -   Connect your GitHub repository to Heroku by searching for the repository name and clicking "Connect".
    -   Scroll down and click "Deploy Branch" to deploy the app.
7.  **Automatic Deploys (Optional):**
    -   If desired, enable automatic deploys to rebuild the app whenever changes are pushed to GitHub.

### Forking The Repository
You can fork the Guess Weather App repository to create a copy for viewing and editing without affecting the original. Follow these steps:

1.  Navigate to the repository on GitHub.
2.  Click on the "fork" tab in the top right corner.
3.  Click on "create fork" to fork the repository.

### Cloning The Repository
To clone the Guess Weather App repository from GitHub:

1.  Go to the repository and select the "code" tab.
2.  Copy the repository's HTTPS URL.
3.  Open Git Bash and navigate to the desired directory.
4.  Type `git clone` followed by the copied URL and press "enter".

### APIs
The Guess Weather App integrates the following APIs:

-   **OpenWeather API:** Provides real-time weather data for various locations worldwide. This API enables the app to retrieve accurate weather information used in the guessing game.
-   **Google Drive API:** Offers credentials to access files within Google Drive, facilitating secure data management for the application.
-   **Google Sheets API:** Manages data stored in Google Sheets, serving as a database for the program's leaderboard and other relevant information.

For instructions on setting up and connecting these APIs, refer to the provided resources or follow the steps outlined in the Code Institute Love Sandwiches project video and the Youtube tutorial in the Credits.

## Credits 
This project was developed as part of Code Institute's Full Stack Software Development Diploma. Special thanks to:

-   **OpenWeather:** For providing the weather data. [https://home.openweathermap.org/api_keys](https://home.openweathermap.org/api_keys)
-   **Google Sheets API:** For enabling real-time leaderboard and city updates.
-   **Colorama:** For enhancing the terminal output.

### Inspiring Content
-	***Creating a multiple choice quiz in Python | Terminal:*** [here](https://brockbyrdd.medium.com/creating-a-multiple-choice-quiz-in-python-terminal-1c46123b86d5)
-	***How To Use OpenWeather API With Python| Youtube Tutorial :*** [here](https://www.youtube.com/watch?v=knWqyRgLl2o)
-	***Find current weather of any city using OpenWeatherMap API in Python:*** [here](https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/)​
-	***How to create a Leaderboard in Google Spreadsheet:*** [here](https://keepthescore.com/blog/posts/create-google-sheets-leaderboard/)



## Acknowledgements: 
- A very special thanks to Pascal the most helpful person i ever met.  He has helped me tremendously with ideas, fixes and feedback.

- I also want to thank my Mentor Rory-Patrick who gave me so many tips and tricks, and inspired me along the way.

- Also very special thanks to my dog who provided emotional support and times to unwind.

- I thank all my peers in my course, who provided a lot of support and feedback!

- I thank all my family members and friends who not only gave feedback and support but also tested it on their devices.
> Written with [StackEdit](https://stackedit.io/).