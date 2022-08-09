import csv

# open our file
with open("datasets/min_wage_2020.csv", "r") as file:
    reader = csv.reader(file)
    next(file) # skip the header line

    wagesList = []
    for line in reader:
        minWage = float(line[2])
        wagesList.append(minWage)

    wagesList.sort()
    print(wagesList)

    middleIndex = int(len(wagesList) / 2)
    print(f"The middle position is {middleIndex}")

    median = wagesList[middleIndex]
    print(f"The median minimum wage is {median}")

