# from <file> import <class>
from video_game import VideoGame

# instantiate the VideoGame class (create objects based on...)
fallout = VideoGame("Fallout 76", "Action", 100, True, True)

# interact with the fields of the object
# fallout.name = "Fallout 76"
# fallout.availableOnPC = True
# fallout.availableOnConsole = True
# fallout.howLongToBeat = 100
# fallout.genre = "Action"

fallout.printInfo()
print() # new line

# instantiate a VideoGame object using a constructor!
eldenRing = VideoGame("Elden Ring", "Souls", "100", True, True)
eldenRing.printInfo()









