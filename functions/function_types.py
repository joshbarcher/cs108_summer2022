# create a few variables with numbers
num1, num2, num3, num4 = -2, 10, -8, 20

# find the smallest number (min() returns the smallest of the inputs to the function)
smallest = min(num1, num2, num3, num4)

# print out the smallest number (as an f-string)
print(f"The smallest is {smallest}")

# print out the smallest number (using several calls to print())
print("The smallest number in [15, 2, 13, 11, 0] is ")
print(min(15, 2, 13, 11, 0))

# print out the smallest number using a single call to print()
print("The smallest number in [5, 4, 3, 1, 2] is", min(5, 4, 3, 1, 2))

# print out the smallest number using string concatenation
print("The smallest number in [18, 100, 12, 5] is " + str(min(18, 100, 12, 5)))

print("Thanks for running my program")

