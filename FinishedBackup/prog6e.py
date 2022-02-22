'''
Created on Thurs Feb 18 9:21:47 2022

@author: C. Schulz

Description: Guessing game with numbers 1-10

Saved as prog6e.py
'''

import random

choiceBot = random.randrange(1,11)
timesGuessed = 0

while True:
    timesGuessed += 1
    yourChoice = int(input('Choose A Number 1-10: '))
    if yourChoice > 10 or yourChoice < 0:
        print('Not A Valid Number. Choose Again.')
        continue
    elif choiceBot == yourChoice:
        print(f'You guessed it! It only took you {timesGuessed} times to guess the correct number!')
        break
    elif choiceBot != yourChoice:
        yourChoice = print('Sorry! Guess Again')
        continue