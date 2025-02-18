# search function that takes "genre" or "actor" as input and searches through movies dict depending an the user choice


from data.movie_data import movies

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
    tryAgain = input("Sorry I couldn't find anything. Do you want to try again? y/n ")
    if tryAgain == "y":
        search(input("Do you want to search by genre or actor? "))

# search function that takes genre or actor as input
def search(genreOrActor):
    result = False
    if genreOrActor == "genre":
        genre = input("Which genre do you want to look for? ")
        for movie in movies:
            if genre in movies[movie][0]:
                result = True
                printResults(movie)
        # if nothing is found result stays False
        if result == False:
            tryAgain()

    elif genreOrActor == "actor":
        actor = input("Which actor do you want to look for? ")
        for movie in movies:
            if actor in movies[movie][1]:
                result = True
                printResults(movie)
        # if nothing is found result stays False
        if result == False:
            tryAgain()

    # if user writes anything else than "actor" or "genre"
    else:
        print("Sorry I can only look for actors or genres. Let's try this again, shall we?")
        search(input("Do you want to search by genre or actor? "))
