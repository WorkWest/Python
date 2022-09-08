import random

import pyinputplus as pyip

user_guess = pyip.inputNum("Guess a number between 1 and 100: ")

machine_number = random.randrange(1,100)

counter = 0

play_again = True

while play_again == True:
  while user_guess != machine_number:
    while user_guess < machine_number:
      print("Too low!")
      user_guess = pyip.inputNum("Guess again: ")
      counter += 1
    while user_guess > machine_number:
      print("Too High!")
      user_guess = pyip.inputNum("Guess again: ")
      counter += 1
    print(f"You did it in {counter} tries!")
    play_again = input("Would you like to play again? (True or False)")
  