from components.search import search

# TODO: implement a choice to terminate the programm

def start():
    userChoice = input("Do you want a movie recommendation for tonight? y/n ")
    if userChoice == "n":
        print("Ok. If you change your mind, you know where to find me!")
    elif userChoice == "y":
        genreOrActor = input("Do you want to search by genre or actor? ")
        search(genreOrActor)
    else:
        print("Sorry, I can only take y, n or c as an answer. Please try again")
        start()