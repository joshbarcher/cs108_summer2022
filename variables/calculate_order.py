# assign our initial values
subTotal = 10.99
taxRate = 0.095

# calculate the tax
taxOwed = subTotal * taxRate

# print out the old-fashioned way!
# print(taxOwed)
# print("You owe $" + str(taxOwed) + " in taxes")

# print out using f-strings
print(f"{subTotal} * {taxRate} = {taxOwed}")
print(f"You owe ${taxOwed} in taxes")

# show the total
total = subTotal + taxOwed
print(f"Your total is ${total}")
