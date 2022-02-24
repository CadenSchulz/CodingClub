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

    # Variables/Times Rolled Per 2 Numbers
x = 1
scoreTwo = 0
scoreThree = 0
scoreFour = 0
scoreFive = 0
scoreSix = 0
scoreSeven = 0
scoreEight = 0
scoreNine = 0
scoreTen = 0
scoreEleven = 0
scoreTwelve = 0

    # 2 Times: Picking Numbers 1-6 Randomly 1000 Times
for x in range(1,1001):
    pick1 = random.choice(list1)
    pick2 = random.choice(list1)
    x += 1
        # Pick For Two -- Adds 1 To How Many Times Two Was Rolled
    if pick1 + pick2== 2:
        scoreTwo += 1
        # Pick For Three -- Adds 1 To How Many Times Three Was Rolled
    elif pick1 + pick2== 3:
        scoreThree += 1
        # Pick For Four -- Adds 1 To How Many Times Four Was Rolled
    elif pick1 + pick2== 4:
        scoreFour += 1
        # Pick For Five -- Adds 1 To How Many Times Five Was Rolled
    elif pick1 + pick2== 5:
        scoreFive += 1
        # Pick For Six -- Adds 1 To How Many Times Six Was Rolled
    elif pick1 + pick2== 6:
        scoreSix += 1
        # Pick For Seven -- Adds 1 To How Many Times Seven Was Rolled
    elif pick1 + pick2== 7:
        scoreSeven += 1
        # Pick For Eight -- Adds 1 To How Many Times Eight Was Rolled
    elif pick1 + pick2== 8:
        scoreEight += 1
        # Pick For Nine -- Adds 1 To How Many Times Nine Was Rolled
    elif pick1 + pick2== 9:
        scoreNine += 1
        # Pick For Ten -- Adds 1 To How Many Times Ten Was Rolled
    elif pick1 + pick2== 10:
        scoreTen += 1
        # Pick For Eleven -- Adds 1 To How Many Times Eleven Was Rolled
    elif pick1 + pick2== 11:
        scoreEleven += 1
        # Pick For Twelve -- Adds 1 To How Many Times Twelve Was Rolled
    elif pick1 + pick2== 12:
        scoreTwelve += 1

        # Percentages For Each Number Rolled
    percentageTwo = scoreTwo/1000 * 100
    percentageThree = scoreThree/1000 * 100
    percentageFour = scoreFour/1000 * 100
    percentageFive = scoreFive/1000 * 100
    percentageSix = scoreSix/1000 * 100
    percentageSeven = scoreSeven/1000 * 100
    percentageEight = scoreEight/1000 * 100
    percentageNine = scoreNine/1000 * 100
    percentageTen = scoreTen/1000 * 100
    percentageEleven = scoreEleven/1000 * 100
    percentageTwelve = scoreTwelve/1000 * 100
    
    # Output For Percentages And How Many Times Each Number Was Rolled Randomly
print('\n')
print('Rolling Two Dice 1000 Times...')
print('\n')
print("{:9s} {:9s} {:9s} {:9s} {:9s} {:9s} {:9s} {:9s} {:9s} {:9s} {:9s}".format('TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','ELEVEN','TWELVE'))
print("{:9s} {:9s} {:9s} {:9s} {:9s} {:9s} {:9s} {:9s} {:9s} {:9s} {:9s}".format('-----', '-----', '-----', '-----', '-----', '-----','-----', '-----', '-----', '-----', '-----'))
print("{} {:9d} {:9d} {:10d} {:9d} {:9d} {:9d} {:9d} {:8d} {:9d} {:9d}".format(scoreTwo, scoreThree, scoreFour, scoreFive, scoreSix, scoreSeven, scoreEight, scoreNine, scoreTen, scoreEleven, scoreTwelve))
print("{:0.1f} {} {:7.1f} {} {:7.1f} {} {:7.1f} {} {:7.1f} {} {:7.1f} {} {:7.1f} {} {:7.1f} {} {:7.1f} {} {:7.1f} {} {:7.1f} {}".format(percentageTwo, '%', percentageThree, '%', percentageFour, '%', percentageFive, '%', percentageSix, '%', percentageSeven, '%', percentageEight, '%', percentageNine, '%', percentageTen, '%', percentageEleven, '%', percentageTwelve, '%'))
print('\n')