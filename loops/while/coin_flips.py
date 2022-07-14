# flip coins, printing their values to the console (heads or tails)
# stop when we see three heads in *** a row ***

import random

heads = 0
tails = 0

# loop while the number of heads has not yet reached 3 in total
while heads < 3:
    # flip the coin
    flip = random.randint(1, 2) # 1 = heads, 2 = tails
    # print(f"Random number is {flip}")

    if flip == 1:
        heads += 1
        print(f"The coin came up heads ({heads} total)")
    elif flip == 2:
        tails += 1

        # reset our heads counter to zero (consecutive heads)
        heads = 0

        print(f"The coin came up tails ({tails} total)")

# this code will run after the loop
print("Thanks for playing my game")




