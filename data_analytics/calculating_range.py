# the csv module makes working with the csv file easier
import csv

with open("datasets/min_wage_2020.csv", "r") as file:
    reader = csv.reader(file)

    # remove the top row of our dataset (headers)
    next(file)

    minWage = 1000 # this is an impossibly high starting value
    maxWage = 0

    # these variables hold the state with the min and max minimum-wage
    stateWithMin = ""
    stateWithMax = ""

    # loop over each row (record) in the file
    for record in reader:
        state = record[1]
        minWageByState = float(record[2])

        # update the smallest seen so far
        if minWageByState < minWage:
            minWage = minWageByState
            stateWithMin = state

        # update the largest seen so far
        if minWageByState > maxWage:
            maxWage = minWageByState
            stateWithMax = state

    # store the range in a tuple (like a list, but different)
    range = (minWage, maxWage)
    stateTerritoryRange = (stateWithMin, stateWithMax)
    print(f"Range is {range}")
    print(f"States/territories are {stateTerritoryRange}")

