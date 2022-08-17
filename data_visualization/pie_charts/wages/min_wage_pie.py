import matplotlib.pyplot as plt
import csv

with open("min_wage_2020.csv", "r") as file:
    reader = csv.reader(file)
    next(file) # skip the header line

    # counters for states that match the fed. min. wage or not
    fedMinWage = 0
    lessThenMinWage = 0
    greaterThenMinWage = 0

    for line in reader:
        minWage = float(line[2])

        if minWage == 7.25:
            fedMinWage += 1
        elif minWage > 7.25:
            greaterThenMinWage += 1
        else:
            lessThenMinWage += 1

    print(f"States/territories that match the federal min. wage: {fedMinWage}")
    print(f"States/territories less than the federal min. wage: {lessThenMinWage}")
    print(f"States/territories greater than the federal min. wage: {greaterThenMinWage}")

    # provide a list of numbers and a list of labels
    minWages = [fedMinWage, lessThenMinWage, greaterThenMinWage]
    pieLabels = ["Min Wage = 7.25", "Min Wage < 7.25", "Min Wage > 7.25"]

    plt.pie(minWages, labels=pieLabels, autopct="%.0f%%")
    plt.title("Minimum Wage in US States/Territories - 2020")
    plt.show()
