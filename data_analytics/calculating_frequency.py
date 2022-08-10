import csv

# open our file, wrap it in a csv reader, and remove the header line
with open("datasets/min_wage_2020.csv", "r") as file:
    reader = csv.reader(file)
    next(file)

    # count the frequencies using a dictionary
    frequencies = {}

    for line in reader:
        minWage = float(line[2])

        # if we haven't seen this minimum wage before, enter a new key/value
        if not minWage in frequencies:
            frequencies[minWage] = 1
        else: # else, increment an exist key/value
            frequencies[minWage] += 1

    # print our results
    print("Min Wage - Frequency")
    for minWage in frequencies:
        count = frequencies[minWage]

        print(f"{minWage} - {count}")

