# printing a rectangle of asterisks
print("Welcome to my program")

for i in range(1, 5): # loop 1-4 times
    for j in range(1, 4): # loop 1-3 times
        print("*", end="")
    print() #new line
print()

# printing a multiplication table (from 0 to 10)
for i in range(0, 11):
    for j in range(0, 11):
        num = i * j

        if num < 10: # single digit
            print("0" + str(num), end=" ")
        else: # double digit
            print(num, end=" ")
    print()


# using nested loops with user input
