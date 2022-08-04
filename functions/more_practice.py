# import the pi constant from the math module
from math import pi

# define a few functions that calculate geometric areas
def areaOfRectangle(length, width):
    # defensive programming
    if length <= 0 or width <= 0:
        return None # None represents a missing area for the rectangle

    return length * width

def areaOfCircle(radius):
    if radius <= 0:
        return None

    return pi * radius ** 2

# call our functions and assign the returned values to a variable
rectArea = areaOfRectangle(-3, -2)
circleArea = areaOfCircle(-6)

if rectArea == None:
    print("Non-positive sides of a rectangle are not defined")
else:
    print(f"Rect area is {rectArea}")

if circleArea == None:
    print("Non-positive radius of a circle is not defined")
else:
    print(f"Circle area is {circleArea}")

