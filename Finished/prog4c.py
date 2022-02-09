'''
Created on Mon Feb 2 10:54:32 2022

@author: C. Schulz

Description: Telling whether a number is factor of another

Saved as prog4c.py
'''

# Imports For Cleaner Output Aesthetic
from time import sleep

# Asking For Two Positive Integers
x = int(input('First Number (Positive Integer): '))
sleep (0.5)
y = int(input('Second Number (Positive Integer): '))

# Variables
ans = y//x
rem = y%x

# Computing Whether or Not The Two Integers are Factors
if ans == 0 or rem >0:
    sleep(0.5)
    print('These two integers ARE NOT factors of each other.')
    sleep(0.5)
else:
    sleep(0.5)
    print('These two integers ARE factors of each other.')
    sleep(0.5)