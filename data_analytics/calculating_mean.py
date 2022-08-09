import csv

# open our file
with open("datasets/min_wage_2020.csv", "r") as file:
    reader = csv.reader(file)
    next(file) # skip the header line

    # variables to help calculate the mean
    sum = 0
    recordCount = 0

    # loop over all the lines, add up the min wages
    for line in reader:
        minWage = float(line[2])
        print(minWage)

        # add the minWage to the sum of wages
        sum += minWage

        # increment the number of lines in the file
        recordCount += 1

    # calculate the average (aka the "mean")
    print(f"Read {recordCount} records!")

    mean = sum / recordCount
    mean = round(mean, 2)
    print(f"The mean minimum wage in the {recordCount} states/territories is ${mean}")
