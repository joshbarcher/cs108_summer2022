# open the speech document
with open("speech.txt", "r") as file:
    # print out the lines of the speech
    lines = file.readlines()
    print("Lines in file", len(lines))
    print() # new line

    for line in lines:
        print(line, end="")
