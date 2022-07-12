# import the math module, with functions that contain math operations
import math

# ask the user for a number
number = int(input("Enter a number: "))

# then calculate and print the square root of the number
if number == 0:
    print("The sqrt of zero is zero!")
elif number < 0:
    print("The sqrt of a negative is not real")
else:
    # this is a catch-all if the conditions above are all false
    print("The sqrt is", math.sqrt(number))

