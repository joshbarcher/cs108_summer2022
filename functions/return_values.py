# define some functions that add numbers
def increment(num):
    num += 1
    return num

def adder(oper1, oper2):
    sum = oper1 + oper2
    return sum

# define a function that gives the negation of a number (10 becomes -10, -2 becomes 2, 3 becomes -3, ...)
def invert(number):
    # invert
    result = number * -1
    return result

newNumber = increment(100)
print(f"Number after incrementing is {newNumber}")

newNumber = increment(newNumber)
print(f"Number after incrementing is {newNumber}")

# try adding 10 to 11 using our adder() function and print the result!
print(adder(10, 11))

added = adder(10, 11)
print(f"Result of adding is", added)
print(f"Result of adding is", adder(10, 11))

inverted = invert(10)
print(f"The negation of 10 is {inverted}")
