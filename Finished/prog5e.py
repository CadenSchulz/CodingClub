'''
Created on Mon Feb 11 11:43:06 2022

@author: C. Schulz

Description: Square Root of An Inputted Number

Saved as prog5e.py
'''

# Imports
import math
from math import sqrt

# Looping
while True:

    # Variable
    number = int(input('Enter A Number: '))

    # Calculating The Square Roots
    if number < 0:
        print(number, 'does not have a square root. Please try again...')
        continue
    else:
        root = math.sqrt(number)
        print(f'The Square Root of {number} is {root}.')
        break