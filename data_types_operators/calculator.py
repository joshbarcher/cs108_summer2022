# read in an x & y value
x = input("Enter a value for variable x: ")
y = input("Enter a value for variable y: ")
z = input("Enter a value for variable z: ")

# convert strings to integers
x = int(x)
y = int(y)
z = int(z)

# calculate x + (y * z)
# order of operations is PEMDAS
result = (x + y) * z
print("Result", result)

division = x / y
floorDivision = x // y

print("Division result", division)
print("Floor division result", floorDivision)

# remainder operator (aka 'mod' or 'modulus')
mod = x % y
print(f"{x} % {y} = {mod}")

expression = -(10 * -3) * -20
print(expression)






