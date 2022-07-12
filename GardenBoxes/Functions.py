from os import system, name
from GardenOptions import *
import time


def clear():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def welcomeVeg():
    print("Welcome to Generic Garden Store. Here we can calculate how much of a certain vegetable you can plant in your garden.")
    time.sleep(1)

    print("Please make a selection below on what you would like to do:\n a) Calculate veggies in your garden\n b) View List of Available Vegetables\n c) Add Vegetable\n d) Quit")
    answer = input().lower()

    return answer


def calcVeg():
    vegGo = True
    length = input(
        "I'm going to need some dimensions from you to get started to find the area.\nFirst, give me the length of your garden: ")

    time.sleep(.5)

    width = input("Next give me the width of the garden: ")

    area = int(length) * int(width)

    print("Calculating")
    time.sleep(.75)
    print(".")
    time.sleep(.75)
    print(".")
    time.sleep(.75)
    print(".")
    time.sleep(.75)

    print(f"The area of your garden box is {area}")

    while vegGo:

        print("Which would you like to do:\n a) Find Out How Much of a Certain Vegetable I Can Plant\n b) I Am Done Here")
        areaChoice = input().lower()

        if areaChoice == 'a':
            print("Did you need to see the available vegetables? Y/N")
            seeVeg = input().lower()

            if seeVeg == 'y':

                showVeg()

            elif seeVeg == 'n':
                print("Which vegetable did you want to choose?")
                vegChoice = input().lower()

                print(f"The vegetable you chose is {vegChoice}")
                time.sleep(1)

                totalVeg = foodArea[vegChoice] * area

                print(
                    f"Based on your choice, you will be able to plant {totalVeg} {vegChoice} in your garden box that is {area} square feet.")
            else:
                errorVeg()

        elif areaChoice == 'b':
            vegGo = False
        else:
            errorVeg()
    print("")


def errorVeg():
    print("Incorrect input, please enter one of the provided choices.")
    time.sleep(1.5)
    print("")


def printStuff():
    print("Does calling functions work?")


def showVeg():
    print("Here are the available vegetables:")

    print("")

    for veg in foodList:
        print(f"{veg}: {foodArea[veg.lower()]} per sq ft")

    print("")


def updateVeg():
    print("Here you can add to the list of vegetables already stored. You will also need to know how much of said vegetable can be planted per square foot.")

    newVeg = input(
        "First, what is the name of the vegetable you are looking to add: ")
    time.sleep(.5)
    print("")

    newVegArea = input(
        "Next, how much of that vegetable can be planted per square foot: ")
    time.sleep(.5)

    print("Adding now. Remember that the exact upper and lower case will be stored. You can view the vegetables from the main menu and change them later if you'd like.")

    print("")

    time.sleep(1.5)

    foodList.append(newVeg)

    foodArea.update({newVeg.lower(): newVegArea})

    print("Inputs received, I will store them for later use.")

    print("")
