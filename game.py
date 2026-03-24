#!/usr/bin/env python3
"""
Simple Number Guessing Game

The computer generates a random number between 1 and 100.
The player has to guess the number with hints provided.
"""

import random

number = random.randint(1, 100)
guess = 0
attempts = 0

print("Guess a number between 1 and 100!")
 
while guess != number:
      guess = int(input("Enter your guess: "))
      attempts += 1

      if guess < number:
          print ("Let's try a higher number.")
      elif guess > number:
          print ("Nope.The number is lower.")
      else:
          print ("Correct! You needed", attempts, "attempts to guess the number.")

      if guess > 100 or guess < 1:
          print ("Please enter a number between 1 and 100.")
          attempts -= 1
        
    