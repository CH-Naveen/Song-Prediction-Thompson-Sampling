# Song-Prediction-Using-Machine-Learning
Song Prediction using Thompson Sampling Algorithm in Reinforcement Learning


Songs of various generes from Kaggle Dataset was used to select songs according the users interests.
Input from user was taken at real time  (Like / Dislike ) after each song and based on the previous input a random song was choosen from the liked genere.

Extension of this project includes:

1. A proper UI by creating a simple REST API. Flask can be used to create a simple API where the user gives his response via an API post request and gets a new suggestion in the API’s response.
2. The link in the URI can be used to play the song to the user instead of just showing the details, which helps the user give better feedback in each round, leading to better recommendations overall.
