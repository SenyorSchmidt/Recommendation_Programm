from components.search import searchByGenre

def start():
    userChoice = input("Do you want a movie reecommendation for tonight? y/n ")
    if userChoice == "n":
        print("Ok. If you change your mind, you know where to find me!")
    elif userChoice == "y":
        genreOrActor = input("Do you want to search by genre or actor? ")
        if genreOrActor == "genre":
            searchByGenre()
    else:
        print("Sorry, I can only take y or no as an answer. Please try again")
        start()