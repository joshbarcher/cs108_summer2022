cities = ["Manhattan", "San Diego", "Seattle", "Long Beach", "Calistoga", "Las Vegas", "Tacoma",
          "Puyallup", "Arlington", "Edmonds"]

# access elements in the list
thirdCity = cities[2]
thirdCity = thirdCity.upper()
print(f"The third city is {thirdCity}")
print(f"The fourth city is {cities[3]}")

# change elements in the list
cities[0] = "Chelan"
cities[1] = "Leavensworth"

print(cities)

# print out the cities all in uppercase, one per line
for index in range(0, len(cities)):
    cityInCaps = cities[index]
    print("City:", cityInCaps.upper())
