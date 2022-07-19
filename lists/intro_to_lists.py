# ask the user repeatedly for their favorite movies, stopping when they say so
moviesList = [] # this is an empty list
movieName = ""

while movieName != "stop":
    # ask the user for a movie
    movieName = input("Enter a favorite movie (or stop to end the program): ")

    # add the movie to our list
    if movieName != "stop":
        moviesList.append(movieName)

# print the number of favorite movies that were entered
numMovies = len(moviesList)
print(f"You have {numMovies} favorite movies")
print(moviesList)

