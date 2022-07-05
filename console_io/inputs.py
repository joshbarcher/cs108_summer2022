# write a program that gathers information about our user and prints it back to them
fullName = input("Enter your full-name: ")
age = input("Enter your age: ")
swimming = input("Do you like to swim? (True/False) ")
number = input("Enter your favorite number: ")

print() # a new line
print("Your name is", fullName)
print("Your age is", age)
print("Do you like swimming?", swimming)

# print out the favorite number squared
squared = int(number) ** 2
print("You favorite number squared is", squared)

# convert our swimming variable data-type from string to boolean
# swimming = bool(swimming)
# print(swimming)

# this is an if statement
if swimming == "True":
    print("You should go swimming at American Lake!")
else:
    print("Maybe go see a movie instead!")




