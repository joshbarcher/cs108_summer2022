import matplotlib.pyplot as plt

xValues = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1,
           0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
yValues = []

# calculate the squares of x
for x in xValues:
    y = x ** 2
    yValues.append(y)

plt.plot(xValues, yValues)
plt.grid(True, which='both')
plt.show()

