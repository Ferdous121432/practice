import random

while True:
    choice = input('Roll the dice? (y/n): ')
    if choice.lower() == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"You rolled a {dice1} and a {dice2}.")
    elif choice.lower() == 'n':
        print("Maybe next time!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
