# name is a global variable (available everywhere, inside of functions as well)
name = input("Enter your name: ")

def readUserAddress():
    # address is a local variable (only available in this function)
    address = input(f"Hi, {name}, Enter your address: ")
    print(f"You entered {address}")

readUserAddress()
print(f"You entered {address}")

