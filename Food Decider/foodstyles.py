import random

foodStyles = [
    "Sushi",
    "Pizza",
    "Burgers",
    "Noodles",
    "Pasta",
    "Chinese",
    "Thai",
    "Indian",
    "Salads",
    "Smoothies",
    "Suffer",
    "Spanish",
    "Greek",
    "Mexican",
    "Cajun"
]

print("Are you feeling indecisive about what you want to eat today?\nY/N?")
decision = input().upper()

if decision == 'Y':
    goEat = random.choice(foodStyles)
    print(f"You should go and eat {goEat}")
if decision == 'N':
    print("Guess you've got it all figured out.")
