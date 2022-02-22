'''
Created on Thurs Feb 18 9:21:47 2022

@author: C. Schulz

Description: Guessing game with numbers 1-10

Saved as prog6e.py
'''
    # Imports
import random

    # Variables/Defining Range and Guess Count
choiceBot = random.randrange(1,11)
timesGuessed = 0

    # Picking A Number 1-10
while True:
    timesGuessed += 1
    yourChoice = int(input('Choose A Number 1-10: '))
        # Seeing If Chosen Number Ranges From 1-10
    if yourChoice > 10 or yourChoice < 0:
        print('Not A Valid Number. Choose Again.')
        continue
        # Output For Guessing The Correct Number/Showing Guess Count
    elif choiceBot == yourChoice:
        print(f'You guessed it! It only took you {timesGuessed} times to guess the correct number!')
        break
        # Output For Guessing The Incorrect Number
    elif choiceBot != yourChoice:
        yourChoice = print('Sorry! Guess Again')
        continue