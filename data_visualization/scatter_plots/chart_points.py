import matplotlib.pyplot as plt
import csv

with open("points.csv", "r") as file:
    reader = csv.reader(file)

    xValues = []
    yValues = []

    # read the x,y components into our lists
    for line in reader:
        xValues.append(float(line[0]))
        yValues.append(float(line[1]))

    # chart them using a scatter plot
    plt.scatter(xValues, yValues)
    plt.show()
