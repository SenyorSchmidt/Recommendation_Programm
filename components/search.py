# 2 search functions: 1. search by genre, 2. search by actor

from data.movie_data import movies

def searchByGenre():
    genre = input("Which genre do you want to look for? ")
    for movie in movies:
        if genre in movies[movie][0]:
            print("Title:")
            print(movie)
            print("\n" + "Actors:")
            for actor in movies[movie][1]:
                print(actor)
            print("\n" + "Description:")
            print(movies[movie][2] + "\n")
    print("Sorry I couldnt find anything. Lets try again")
    searchByGenre()

