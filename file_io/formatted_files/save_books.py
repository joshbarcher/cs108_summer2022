# define a function that saves a single book to a file
def saveABook():
    print("Please enter the following information on a book")
    title = input("Enter a title: ")
    yearReleased = int(input("Enter a year released: "))
    author = input("Enter the author: ")
    pages = int(input("Enter the number of pages: "))

    with open("books.csv", "a") as writer:
        writer.write(f"{title},{yearReleased},{author},{pages}\n")
        print(f"The book {title} written to books.csv")

moreBooks = "Yes"
while moreBooks == "Yes":
    # save a new book to the file
    saveABook()

    # should we continue?
    moreBooks = input("Should we continue (Yes/No)? ")

