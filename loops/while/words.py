# repeatedly prompt the user to enter words
# until the word they enter is less than 5 characters

word = input("Enter a word: ")
lenWord = len(word)
print("You entered", word)

# this condition needs to be true to loop and continue
while lenWord >= 5:
    word = input("Enter a word: ")
    lenWord = len(word)
    print("You entered", word)

