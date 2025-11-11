import random

GUESSED_NUMBER = random.randint(1, 100)

while True:
    guess = input("Guess a number between 1 and 100 (or 'q' to quit): ")
    if guess.lower() == 'q':
        print("Thanks for playing!")
        break
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    guess = int(guess)
    if guess < GUESSED_NUMBER:
        print("Too low!")
    elif guess > GUESSED_NUMBER:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")
        break
