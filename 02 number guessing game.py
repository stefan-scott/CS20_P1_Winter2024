# Number Guessing Game
# Mr. Scott
# April 15, 2024
# A game where the user tries to guess a number (1-100)

import random

# Start by selecting a "hidden number"
hidden_number = random.randint(1,100)

# Ask the user for their guess
user_guess = input("Guess a number: ")  #STR
user_guess = int(user_guess) #INT

while user_guess != hidden_number:
    if user_guess > hidden_number:
        print("Too high!")
    else:
        print("Too low!")
    user_guess = int(input("Guess a number: "))

print("You got it!")