# create a few variables to hold our user inputs and our sum
sum = 0

# loop while our sum is not yet complete
while sum <= 42:
    userInputNum = int(input("Enter a number: "))
    sum = sum + userInputNum # another way to write this is sum += userInputNum
    print(f"The sum is currently {sum}")

print(f"The final sum is {sum}")

