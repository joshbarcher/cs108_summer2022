# sum together several numbers (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55)

# accumulator pattern in action!
product = 0
for num in range(1, 11):
    print(num)
    product = product * num

print(f"Factorial is {product}")

