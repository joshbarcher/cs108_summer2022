# In this file we are practicing input and output on the Python console.
# Author: Josh Archer
# Date: 8/8/2022
# File: console_io.py

# try using nifty ways to call print()
firstName = "Josh"
lastName = "Archer"
middleInit = "B"

# pass three 'literal' values to print
print("Hello", "Josh", "How are you?")

# pass variables to print
#      (Josh)      (B)       (Archer)
print(firstName, middleInit, lastName)

# pass variables and 'literal' values to print
print("Mr.", firstName, lastName, "is 44 years old this year!")

# example of string concatenation
month = "July "
day = "5th"

print(month + day)
print("June " + "14th")
print("The " + day + " of " + month)

# dealing with concatenation of numbers and booleans
classPrefix = "CS"
classNumber = 108

print(classPrefix + str(classNumber))
print("Did I have fun on the 4th? " + str(True))

# alternatively!
print(classPrefix, classNumber)
print("Did I have fun on the 4th?", True)

