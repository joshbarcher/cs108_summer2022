# declare a few sets
colorsSet = {"green", "red", "red", "blue", "pink", "red", "blue", "blue"}
numbersSet = {42, 24, 7, 3, 19, 34, 13, 12}

# print them out
print(colorsSet)
print(numbersSet)
print()

# printing out elements by position (does not work!)
# print(colorsSet[0])
# print(colorsSet[1])

# loop over them
for color in colorsSet:
    print(f"Color: {color}")

if 21 in numbersSet:
    print("Found 21!")
else:
    print("Did not find 21!")

