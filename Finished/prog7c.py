'''
Created on Thurs Feb 24 3:39:52 2022

@author: C. Schulz

Description: Rolling a dice 5000 times and counting how many times a number was rolled

Saved as prog7c.py
'''

    # Imports
import random

    # List Of Numbers On Dice
list1 = [1,2,3,4,5,6]

    # Variables/Times Flipped Per Number
x = 1
scoreOne = 0
scoreTwo = 0
scoreThree = 0
scoreFour = 0
scoreFive = 0
scoreSix = 0

    # Picking Numbers 1-6 Randomly 5000 Times
for x in range(1,5001):
    pick = random.choice(list1)
    x += 1
        # Pick For One -- Adds 1 To How Many Times One Was Flipped
    if pick == 1:
        scoreOne += 1
        # Pick For Two -- Adds 1 To How Many Times Two Was Flipped
    elif pick == 2:
        scoreTwo += 1
        # Pick For Three -- Adds 1 To How Many Times Three Was Flipped
    elif pick == 3:
        scoreThree += 1
        # Pick For Four -- Adds 1 To How Many Times Four Was Flipped
    elif pick == 4:
        scoreFour += 1
        # Pick For Five -- Adds 1 To How Many Times Five Was Flipped
    elif pick == 5:
        scoreFive += 1
        # Pick For Six -- Adds 1 To How Many Times Six Was Flipped
    elif pick == 6:
        scoreSix += 1

        # Percentages For Each Number Flipped
    percentageOne = scoreOne/5000 * 100
    percentageTwo = scoreTwo/5000 * 100
    percentageThree = scoreThree/5000 * 100
    percentageFour = scoreFour/5000 * 100
    percentageFive = scoreFive/5000 * 100
    percentageSix = scoreSix/5000 * 100
    
    # Output For Percentages And How Many Times Each Number Was Flipped Randomly
print('\n')
print("{:14s} {:14s} {:14s} {:14s} {:14s} {:14s}".format('ONE', 'TWO','THREE','FOUR','FIVE','SIX'))
print("{:14s} {:14s} {:14s} {:14s} {:14s} {:14s}".format('-----', '-----', '-----', '-----', '-----', '-----'))
print("{} {:14d} {:14d} {:14d} {:14d} {:14d}".format(scoreOne, scoreTwo, scoreThree, scoreFour, scoreFive, scoreSix))
print("{:0.1f} {} {:12.1f} {} {:12.1f} {} {:12.1f} {} {:12.1f} {} {:12.1f} {}".format(percentageOne, '%', percentageTwo, '%', percentageThree, '%', percentageFour, '%', percentageFive, '%', percentageSix, '%'))