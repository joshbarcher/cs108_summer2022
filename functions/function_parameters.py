import random

# function(s) for flipping coins
def flipCoin(coinType):
    # 1 is heads, 2 is tails
    flip = random.randint(1, 2)

    if flip == 1:
        print(f"The {coinType} came up heads")
    else:
        print(f"The {coinType} came up tails")

# numFlips is an integer, coinType is a string
def flipMultipleTimes(numFlips, coinType):
    for i in range(numFlips):
        flipCoin(coinType)

# this is a bad design that doesn't scale well!
# def flipMultipleQuarters(numFlips):
#     # assume we are flipping quarters
#     for i in range(numFlips):
#         flipCoin("quarter")
#
# def flipMultipleDimes(numFlips):
#     # assume we are flipping quarters
#     for i in range(numFlips):
#         flipCoin("dime")
#
# def flipMultiplePennies(numFlips):
#     # assume we are flipping quarters
#     for i in range(numFlips):
#         flipCoin("penny")
#
# def flipMultipleNickels(numFlips):
#     # assume we are flipping quarters
#     for i in range(numFlips):
#         flipCoin("nickel")

# a function to run the program
flipCoin("quarter")
flipCoin("penny")
print()

flipMultipleTimes(5, "quarter")
print()

flipMultipleTimes(7, "dime")
print()

flipMultipleTimes(2, "dollar piece")
print()