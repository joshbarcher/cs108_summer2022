# ask the user for two numbers
numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter a denominator: "))

# then divide them
if denominator != 0:
    divided = numerator / denominator
    divided = round(divided, 2)
    print(f"{numerator} / {denominator} = {divided}")
else:
    print("Division by zero is undefined!")
