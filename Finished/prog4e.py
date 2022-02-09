'''
Created on Mon Feb 6 11:26:47 2022

@author: C. Schulz

Description: Calculating a bowler's average score over three games.

Saved as prog4e.py
'''



# Imports/Functions
from time import sleep

# Cleaner Output Aesthetic
print('.')
sleep(0.5)
print('.')
sleep(0.5)
print('.')
sleep(0.5)

# Variables/Asking For Bowler Information
name = input('Your Name: ')
nameTeam = input('Your Team Name: ')
scoreOne = float(input('First Game\'s Score: '))
scoreTwo = float(input('Second Game\'s Score: '))
scoreThree = float(input('Third Game\'s Score: '))
sum = float(scoreOne) + float(scoreTwo) + float(scoreThree)
average = sum/3

# Cleaner Output Aesthetic
print('.')
sleep(0.5)
print('.')
sleep(0.5)
print('.')
sleep(0.5)

# Outputting Bowling Team Information
print('----------------------')
print('Caden\'s Bowling Alley')
print("{:20s} {:20s}".format(name, nameTeam))
print('Game 1: ', int(scoreOne))
print('Game 2: ', int(scoreTwo))
print('Game 3: ', int(scoreThree))
print("{} {:.3f}".format('Three Game Average: ', average))
print('----------------------')