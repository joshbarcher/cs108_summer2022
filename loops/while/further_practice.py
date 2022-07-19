# print powers of 2 using a while loop (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024)
multipleOfTwo = 2
while multipleOfTwo <= 1024:
    print(multipleOfTwo)
    multipleOfTwo *= 2   # shorthand for multipleOfTwo = multipleOfTwo * 2

print() # new line

# print a pyramid (sort-of) of asterisks (*)
pyramidString = "*"
rowsPrinted = 0
numSpaces = 19
while rowsPrinted < 20: # loop until the pyramid is 12 characters wide
    # increment the number of rows
    rowsPrinted += 1

    # create a number of spaces so the pyramid is shaped correctly
    spaces = " " * numSpaces
    print(spaces + pyramidString)

    # number of spaces should now be one smaller
    numSpaces -= 1

    # add more asterisks to the string (the string is growing)
    pyramidString = "*" + pyramidString + "*"
