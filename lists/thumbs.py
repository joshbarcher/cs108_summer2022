thumbs = [True, True, False, True, False, False, False, True]

# thumbs is our list, thumb is one of the elements in the list

#for-each loop
for thumb in thumbs:
    if thumb == True:
        print("Thumbs up")
    else:
        print("Thumbs down")

#for loop
for index in range(0, len(thumbs)):
    thumb = thumbs[index]

    if thumb == True:
        print("Thumbs up")
    else:
        print("Thumbs down")

