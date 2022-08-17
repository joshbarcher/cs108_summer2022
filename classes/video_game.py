# only declare the VideoGame class in this file
class VideoGame:
    # fields (attributes)
    name = ""
    genre = ""
    howLongToBeat = 0
    availableOnConsole = False
    availableOnPC = False

    # a constructor (a method to instantiate a class)
    def __init__(self, gameName, gameGenre, gameTime, onConsole, onPC):
        self.name = gameName
        self.genre = gameGenre
        self.howLongToBeat = gameTime
        self.availableOnConsole = onConsole
        self.availableOnPC = onPC

    # methods (actions)
    def play(self):
        print(f"You start playing {self.name}")

    def printInfo(self):
        print("*" * 20)
        print(f"Title: {self.name}")
        print(f"Number of hours (on avg) to beat: {self.howLongToBeat}")
        print(f"Is this available on PC? {self.availableOnPC}")
        print("*" * 20)

