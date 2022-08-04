# import the first three functions from my module
from my_console_module import printDivider, printMessage, readInt

# welcome my user
printMessage("Welcome to my calculator", True)
printDivider()

# ask for a few numbers
num1 = readInt("Enter a number: ")
num2 = readInt("Enter a number: ")

# perform a calculation and show the result
sum = num1 + num2
printMessage(f"The sum of {num1} + {num2} = {sum}", True)
