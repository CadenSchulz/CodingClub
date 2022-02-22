'''
Created on Mon Feb 21 11:23:23 2022

@author: C. Schulz

Description: Flipping A Coin 1000 Times

Saved as prog6f.py
'''
import random

list1 = ['Heads', 'Tails']

x = 1
scoreHeads = 0
scoreTails = 0

while x <= 1000:
    pick = random.choice(list1)
    x += 1
    if pick == 'Heads':
        scoreHeads += 1

    elif pick == 'Tails':
        scoreTails += 1

    percentageHeads = scoreHeads/1000 * 100
    percentageTails = scoreTails/1000 * 100
    
print('\n')
print("{:20s} {:20s}".format('HEADS', 'TAILS'))
print("{:20s} {:20s}".format('-----', '-----'))
print("{} {:20d}".format(scoreHeads, scoreTails))
print("{:0.1f} {} {:18.1f} {}".format(percentageHeads, '%', percentageTails, '%'))