# we need the matplotlib and csv modules
import matplotlib.pyplot as plt
import csv

xValues = []
yValues = []

# read from my file and record the points in the file
with open("us_gdp_by_year.csv", "r") as file:
    reader = csv.reader(file)
    next(file) # skip the first line of the file (with headers)

    for line in reader:
        x = int(line[0])
        y = float(line[1])

        xValues.append(x)
        yValues.append(y)

    plt.plot(xValues, yValues)
    plt.xlabel("Year")
    plt.ylabel("GDP")
    plt.title("US GDP 1947-2022")
    plt.show()
