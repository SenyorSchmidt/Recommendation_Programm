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

2.1 components:

The components folder consists of the different components used for the Recommendation Programm.

2.1.1 __init__.py:

This empty .py-file is used to turn the components folder into a package to make it easier to import individual functions from the needed files.

2.1.2 start.py:

The start.py file consists of:
    - an import of the search function and
    - declaration and implementation of the start function

The start function asks the User if a recommendation is wished.
If chosen "y" the start function calls the search function with "genre" or "actor" as a variable, according to the users choice.

If chosen "n" the programm terminates.

Any other choice will result in the recursive calling of the start function, because it can only handle "actor" or "genre" as an input.

