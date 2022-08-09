season = input("Enter a season: ")

# convert user input to lowercase
season = season.lower()

# suggest a seasonal restaurant
restaurant = "Denny's (your input was not valid)"
if season == "fall" or season == "winter":
    restaurant = "Olive Garden"
elif season == "spring":
    restaurant = "Mazatlan"
elif season == "summer":
    restaurant = "Beer Garden"

print(f"You should stop by the {restaurant}")
