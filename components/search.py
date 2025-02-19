# search function that takes "genre" or "actor" as input and searches through movies dict depending an the user choice

from data.movie_data import movies

# TODO: implement a choice to terminate the programm

# function to print out the movie, that fits the search item
def printResults(movie):
    print("Title:")
    print(movie)
    print("\n" + "Actors:")
    for actor in movies[movie][1]:
        print(actor)
    print("\n" + "Description:")
    print(movies[movie][2] + "\n")

def tryAgain():
    tryagain = input("Sorry I couldn't find anything. Do you want to try again? y/n ")
    if tryagain == "y":
        search(input("Do you want to search by genre or actor? "))
    elif tryagain == "n":
        print("Ok. If you change your mind, you know where to find me!")
    else:
        print("Sorry I can only take y or no as an answer")
        tryAgain()

def movieSearch(movies, genreOrActor, int, result):
    if genreOrActor == "exit":
        print("Ok. If you change your mind, you know where to find me!")

    else:
        for movie in movies:
            if genreOrActor in movies[movie][int]:
                result = True
                printResults(movie)
        if result == False:
            tryAgain()


# search function that takes genre or actor as input
def search(genreOrActor):
    result = False
    if genreOrActor == "genre":
        genre = input("Which genre do you want to look for? You can also quit the programm by typing 'exit'. ")
        movieSearch(movies, genre, 0, result)

    elif genreOrActor == "actor":
        actor = input("Which actor do you want to look for?  You can also quit the programm by typing 'exit'. ")
        movieSearch(movies, actor, 1, result)

    # if user writes anything else than "actor" or "genre"
    else:
        print("Sorry I can only look for actors or genres. Let's try this again, shall we?")
        search(input("Do you want to search by genre or actor? "))
