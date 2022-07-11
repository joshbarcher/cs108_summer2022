# create a few variables about taking a walk for exercise
isRaining = True
wearingACoat = False
usingUmbrella = True
planToWalk = 20

if isRaining == True and usingUmbrella == True:
    print("Are you not from Washington?")
else:
    print("Have a fun walk!")

if isRaining == False and wearingACoat == True:
    print("Is it generally cold outside?")
    print("I'm just asking...")

if isRaining == True and wearingACoat == False and planToWalk > 15:
    print("You will get very wet walking that long in the rain")

