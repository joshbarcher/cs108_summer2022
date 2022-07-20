# a list of our ages in the classroom
ages = [44, 34, 19, 19, 21, 29]

listLength = len(ages)
sum = 0

for age in ages:
    sum = sum + age

average = sum / listLength
print(f"The average age in our class is {round(average, 1)} years old!")

