# print the even numbers in the range [1, 100]
num = 1

# loop while num is still in the range
while num <= 100:
    if num % 2 == 0:
        print(f"{num} is even")
    num += 1
print() # new line

# how would you write this same code (above) with a for-loop?
for num in range(1, 101):
    if num % 2 == 0:
        print(f"{num} is even")

