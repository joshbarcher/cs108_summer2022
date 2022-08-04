# open a file for storing contacts
with open("contacts.txt", "a") as file:
    print("Enter contact details")

    name = input("Enter a name: ")
    occupation = input("Enter an occupation: ")

    # write the contact to file
    file.write("***********************\n")
    file.write(name + "\n")
    file.write(occupation + "\n")
    file.write("***********************\n")

