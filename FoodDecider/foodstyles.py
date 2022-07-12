import random
import time
from foodlists import *

keepGoing = True

print("Are you feeling indecisive about what you want to eat today? Y/N?")
decision = input().upper()

if decision == 'Y':

    while keepGoing:
        if decision == 'Y':
            goEat = random.choice(foodStyles)
            print(f"You should go and eat {goEat}")
        elif decision == 'N':
            print("Guess you've got it all figured out.")
            time.sleep(1)
            quit()

elif decision == 'N':
    quit()
