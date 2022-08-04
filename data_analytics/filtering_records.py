import csv

# open up the employee records file
with open("datasets/employee_records.csv", "r", newline="") as badData:
    with open("datasets/cleaned_records.csv", "w", newline="") as cleanData:
        reader = csv.reader(badData)
        writer = csv.writer(cleanData)

        # filter out any bad records
        validPositions = ["Salaried", "Part-time", "Contractor"]
        for line in reader:
            if len(line) != 5:
                # bad record
                print(f"Rejected line with wrong number of fields: {line}")
            elif not line[2] in validPositions:
                # bad record (position is invalid)
                print(f"Rejected line with bad position: {line[2]}")
            else:
                # good record (write the list to a single line in the file)
                writer.writerow(line)
