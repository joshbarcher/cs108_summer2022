# dictionary of movies mapped to running times
movieTimes = {
    "fellowship of the ring": 178,
    "transformers: revenge of the fallen": 150,
    "stranger than fiction": 113,
    "spaceballs": 96,
    "the dark knight": 152,
    "the hobbit": 189
}

# print out the movies
for movie in movieTimes:
    print(movie)
print() # new line

# print out the movies and times
for movie in movieTimes:
    time = movieTimes[movie]
    print(f"{movie} runs {time} minutes")
print() # new line

# look up "values" in the dictionary, by providing "keys"
while True:
    movieName = input("Enter a movie name: ")
    movieName = movieName.lower() # make the search case-insensitive

    if movieName in movieTimes:
        print("Movie found!")
        time = movieTimes[movieName]
        print(f"{movieName} runs {time} minutes")
    else:
        print("Movie not found!")

