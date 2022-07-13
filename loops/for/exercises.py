# print out the characters of our name
fullName = "Josh B. Archer"

for singleCharacter in fullName: # the sequence is a string
    print(singleCharacter)
print() # new line!

# print out a list of our favorite sports teams
sportsTeams = ["Mariners", "Miami Heat", "Seahawks", "Cleveland Cavs", "Los Angeles Lakers"]

for team in sportsTeams:
    print("One of my favorite teams is", team.upper())
print() # new line!

# print out all years from 1900-2000 (the last century)
lastCentury = range(1900, 2001)

for year in lastCentury:
    print(f"Year: {year}")
print() # new line!

# print out all years from 2001-2022 (the current century)
for year in range(2001, 2023):
    print(f"Year: {year}")
print() # new line!

# print out the contents of a file (looking ahead...)
file = open("script.txt", "r")
scriptLines = file.readlines()

# print the line number and text on each line
lineNum = 1
for line in scriptLines:
    totalCharacters = len(line)
    line = line.replace("\n", "")

    print(f"{lineNum}: {line} ({totalCharacters} characters)")
    lineNum += 1

print() # new line!

