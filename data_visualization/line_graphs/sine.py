import matplotlib.pyplot as plt
import math

xValues = []
yValues = []

# calculate our (x,y) points
for i in range(0, 100):
    xValues.append(i * 0.2) # 0.1, 0.2, 0.3, 0.4, 0.5, ... , 30.0

for x in xValues:
    y = math.sin(x)
    yValues.append(y)

# display them
plt.plot(xValues, yValues)
plt.grid(True, which='both')
plt.show()
