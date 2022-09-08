import random

import pyinputplus as pyip

user_guess = pyip.inputNum("Guess a number between 1 and 100: ")

machine_number = random.randrange(1,100)

guesses = 0

while user_guess != machine_number:
  while user_guess < machine_number:
    print("Too low!")
    user_guess = pyip.inputNum("Guess again: ")
    guesses += 1
  while user_guess > machine_number:
    print("Too High!")
    user_guess = pyip.inputNum("Guess again: ")
    guesses += 1

print(f"You did it in {guesses} tries!")