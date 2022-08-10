# we need the matplotlib and csv modules
import matplotlib.pyplot as plt
import csv

# read from my file and record the points in the file
with open("us_gdp_by_year.csv", "r") as file:
    reader = csv.reader(file)

    for line in reader:
        print(line)

