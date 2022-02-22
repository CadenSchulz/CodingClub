'''
Created on Mon Feb 21 11:23:23 2022

@author: C. Schulz

Description: Flipping A Coin 1000 Times

Saved as prog6f.py
'''

    # Imports
import random

    # List Of Heads Or Tails
list1 = ['Heads', 'Tails']

    # Variables/Times Flipped Per Heads Or Tails
x = 1
scoreHeads = 0
scoreTails = 0

    # Picking Heads Or Tails Randomly 1000 Times
while x <= 1000:
    pick = random.choice(list1)
    x += 1
        # Pick For Heads -- Adds 1 To How Many Times Heads Was Flipped
    if pick == 'Heads':
        scoreHeads += 1

        # Pick For Tails -- Adds 1 To How Many Times Tails Was Flipped
    elif pick == 'Tails':
        scoreTails += 1

        # Percentages For Heads/Tails Flipped
    percentageHeads = scoreHeads/1000 * 100
    percentageTails = scoreTails/1000 * 100
    
    # Output For Percentages And How Many Times Heads or Tails Was Flipped Randomly
print('\n')
print("{:20s} {:20s}".format('HEADS', 'TAILS'))
print("{:20s} {:20s}".format('-----', '-----'))
print("{} {:20d}".format(scoreHeads, scoreTails))
print("{:0.1f} {} {:18.1f} {}".format(percentageHeads, '%', percentageTails, '%'))