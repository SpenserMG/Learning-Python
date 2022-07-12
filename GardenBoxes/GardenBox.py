from Functions import *
from GardenOptions import *
import time

keepGoing = True
answer = ""

while keepGoing:

    answer = welcomeVeg()

    if answer == 'a':

        calcVeg()

    elif answer == 'b':

        showVeg()

    elif answer == 'c':

        updateVeg()

    elif answer == 'd':

        keepGoing = False

    else:

        errorVeg()

clear()
