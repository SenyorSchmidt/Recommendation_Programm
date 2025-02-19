** IN PROGRESS **

This is the ReadMe file for my Recommendation Programm.

It's a "Portfolio Project" from the Codecademy Computer Science Course. This Project marks the end of the coding part, before the course continues with databases.

The programm is seperated into multiple components in the "components"-folder. It is done to keep the individual files and functions simple and clean. Addionally it provides the seperation of concerns.

The files include comments with explanations to make it more clear to the reader, how each function works.

No Frameworks or libraries are used, except the standard python library.

1. main.py:

main.py is the main.py file for the programm and consists of:
    - an import of the start function from start.py,
    - declaration and implementation of the main function and
    - the __name__ variable that is set to "__main__"

The main function welcomes the user by printing "Hello User!" and calls the start function, which is imported from /components/start.py

The __name__ variable includes and calls the previously mentioned main function.

2.1. components:

The components folder consists of the different components used for the Recommendation Programm.

2.1.1. __init__.py:

This empty .py-file is used to turn the components folder into a package to make it easier to import individual functions from the needed files.

2.1.2. start.py:

The start.py file consists of:
    - an import of the search function and
    - declaration and implementation of the start function

The start function asks the User if a recommendation is wished.
If chosen "y" the start function calls the search function with "genre" or "actor" as a variable, according to the users choice.

If chosen "n" the programm terminates.

Any other choice will result in the recursive calling of the start function, because it can only handle "actor" or "genre" as an input.

2.1.3 search.py:

The search.py file consists of:
    - an import of the movies dict containing the data about the movies
    - declaration and implementation of the printResults, tryAgain, movieSearch and search functions

The search function takes a genreOrActor variable that is provided by the start function from 2.1.2. start.py. It sets the variable result as False. This is important to determine, if a result was found later and to print the accurate response. If the genreOrActor variable is either genre or actor it asks the user for the wanted name. If genreOrActor fits the words "genre" or "actor" it looks for the provided name in the movies dict at the index 0 or 1 respectively by calling the movieSearch function with the variables movies, genre/actor, 0/1 and result.
If neither "genre" or "actor" is selected it prints out a statement and calls itself again.

the movieSearch function takes movies, genreOrActor, int and result as variables. It checks first if genreOrActor equals to "exit" and terminates itself if thats the case. Otherwise it iterates through the movies dict with a for loop. If the user looks for a genre it looks through the 0th index of the value of the movies dict for the movie key. For an actor it looks through the 1st index. If a result is found, the variable result turn True and the function prints the movie, that fits the pattern.
Otherwise it calls the function TryAgain.

The printResults function takes the movie as an input and prints the Title, Actors and a short description of the movie. It is called by the movieSearch function.

The tryAgain function takes the input of the user if they want to try again. If yes, it calls the search function with the input that is provided by the user. If not, then the programm terminates with a print statement.
If its neither "y" nor "n" the function prints a statement and calls itself again