# create variables for the parts of a name
first = input("Enter first name: ")
last = input("Enter last name: ")
middle = input(f"Enter middle initial - {first} X. {last}: ")

# add a period after the middle initial
middle += "."

# convert my inputs to title-case
first = first.title()
middle = middle.title()
last = last.title()

# only print if the middle is an initial
if len(middle) == 2:
    print(f"{first} {middle} {last}")
else:
    print("Enter a valid middle initial")
