# 2 search functions: 1. search by genre, 2. search by actor

from data.movie_data import movies

def printResults(movie):
    print("Title:")
    print(movie)
    print("\n" + "Actors:")
    for actor in movies[movie][1]:
        print(actor)
    print("\n" + "Description:")
    print(movies[movie][2] + "\n")


def searchByGenre():
    genre = input("Which genre do you want to look for? ")
    result = False
    for movie in movies:
        if genre in movies[movie][0]:
            result = True
            printResults(movie)

    if result == False:
        print("Sorry I couldn't find anything for this genre. Let's try again!")
        searchByGenre()
        
def searchByActor():
    actor = input("Which actor do you want to look for? ")
    result = False
    for movie in movies:
        if actor in movies[movie][1]:
            result = True
            printResults(movie)
    
    if result == False:
        print("Sorry I couldn't find anything for this actor. Let's try again!")
        searchByActor()