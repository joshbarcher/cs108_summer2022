import random

# simulate rolling of dice (typically 4, 6, 8, 10, 12, 20, 100)
diceSides = int(input("Enter a number of sides on a die: "))

# this loop is intentionally infinite
while True:
    number = random.randint(1, diceSides)
    print(f"You rolled {number}")

    if input("Type 'end' to stop rolling: ") == "end":
        break # exit the loop

print("Thanks for playing my game!")


# print out all numbers in [1, 100] except for multiples of 7
for num in range(1, 101):
    # is the current num a multiple of 7
    if num % 7 == 0:
        continue; # go back to the top of the loop and continue the next "iteration"
    else:
        print(num)

