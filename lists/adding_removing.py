import random

# add 10,000 random numbers to a list
randomNums = []

# this loop will run 10,000 times
for i in range(100):
    number = random.randint(1, 10)
    randomNums.append(number)

# at this point we should have a list of 10,000 random numbers
print(randomNums)
lenBefore = len(randomNums)

# let's remove all 2s
while 2 in randomNums:
    randomNums.remove(2)

print(randomNums)
lenAfter = len(randomNums)

removed2s = lenBefore - lenAfter
print(f"We removed {removed2s} 2s")






