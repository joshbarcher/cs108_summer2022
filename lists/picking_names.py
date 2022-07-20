import random

list = ["Josh", "Amanda", "Evan", "Justine", "Kaalid", "Toby"]

# loop once for each position in the list
for i in range(len(list)):
    # print the remaining names
    print("Picking from:", list)

    # pick a random position
    randomIndex = random.randint(0, len(list) - 1)
    print("Random position", randomIndex, "chosen")

    # print out the name at that position
    name = list[randomIndex]
    print("Name:", name)

    # remove the name at that position
    list.remove(name)
