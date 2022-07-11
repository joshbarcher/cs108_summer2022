# get the user input
yearBorn = int(input("Enter the year you were born: "))

# tell the user which generation they belong to
if yearBorn >= 1996 and yearBorn <= 2015:
    print("You are gen Z")
elif yearBorn >= 1977 and yearBorn <= 1995:
    print("You are a millennial")
elif yearBorn >= 1965 and yearBorn <= 1976:
    print("You are generation X")
else:
    print("This program is not sure what generation you belong to...")

print("Thanks for running my program!")

