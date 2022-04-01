# Python_Projects

This folder contains all of the python projects I have completed, and/or are in the process of working on. All of the projects listed are completed except for the Impossible_TTT file.

The 1 player TTT file involves a tic-tac-toe game board which is created using a dictionary and key values 0 - 9. The user will be asked to place an X or an O, and then after a slight delay, the computer will take a turn. The computer turn is accomplished by picking a random number and ensuring that number was not already chosen. 

The 2 player TTT file is the same as the 1 player TTT file, except there is no computer turn, and it is just another user input. 

The impossible TTT file is still a work in progress, but the goal is to make it so that no matter what choices the user makes, the computer will always win or tie. The issue I am facing with this file right now is that for some reason the computer will override spaces that the user had already chosen. Hopefully it is going to be a simple fix and I can get it working properly soon. 

The current weather file connects to the OpenWeatherAPI in order to determine the current weather for a city. I felt it was unreasonable to know the longitude/latitude or zip code of a city off the top of your head, so I also implemented a way to obtain the longitude/latitude values from the name of the city and state (if applicable), along with the country code. This was done by connecting to the Direct Geocoding API. From the resulting information obtained from the API, the current temperature, feels like temperature, minimum temperature, maximum temperature, humidity, and sky description will be printed to the screen. 
