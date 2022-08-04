# open the file for reading
with open("books.csv", "r") as reader:
    linesList = reader.readlines()

    # loop over each line of the file
    mostPages = 0
    for line in linesList:
        # break up the line of the file using split()
        fieldsList = line.split(",")

        year = int(fieldsList[1])
        pages = int(fieldsList[3])

        # if this current book has more pages than the
        # most I have seen so far, than record this as
        # the most pages seen so far
        if pages > mostPages:
            mostPages = pages

    print(f"The longest book was {mostPages} pages!")
