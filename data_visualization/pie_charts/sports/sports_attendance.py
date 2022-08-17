import matplotlib.pyplot as plt
import csv

with open("avg_attend_2021.csv", "r") as file:
    reader = csv.reader(file)

    # a list for teams and avg attendance per team
    allTeams = []
    allAttendance = []

    for line in reader:
        team = line[0]
        sport = line[1]
        attendance = int(line[2])

        print(f"The {team} had {attendance} average attendance in 2021.")

        # build up our lists
        allTeams.append(team)
        allAttendance.append(attendance)

    print(allTeams)
    print(allAttendance)

    plt.pie(allAttendance, labels=allTeams, autopct="%.1f%%")
    plt.show()





