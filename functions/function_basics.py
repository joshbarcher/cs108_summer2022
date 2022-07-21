import random

# declare some functions
def welcomeMessage():
    print("Welcome to my dice rolling program")
    print("Please enter the type of dice below")
    print()

def rollDice():
    print("You are rolling a die")

    # 4, 6, 8, 10, 12, 20, 100 (sides)
    numSides = int(input("Enter a number of sides: "))

    print(f"The dice is {numSides}-sided")
    print("*********************")

    # roll and print the die
    roll = random.randint(1, numSides)
    print(f"The die came up {roll}")

    print("*********************")
    print() # new line!

# this function runs my entire dice rolling program
def myProgram():
    welcomeMessage()

    numDice = int(input("How many dice do you want to roll? "))
    print()

    for i in range(numDice):
        rollDice()

# start my program by calling myProgram()
myProgram()
