import matplotlib.pyplot as plt

# create a dictionary of dice sides to frequencies of the rolls
mapRolls = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

numRolls = 10
with open(f"{numRolls}_rolls.txt", "r") as file:
    # read all lines of the file
    lines = file.readlines()

    for line in lines:
        # read a line in the file
        roll = int(line)

        # increment the frequency of the side of the dice that came up, in the map
        mapRolls[roll] += 1

    print(mapRolls)
