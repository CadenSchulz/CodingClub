'''
Created on Mon Feb 2 10:54:32 2022

@author: C. Schulz

Description: Dividing positive integers and finding the quotient/remainder

Saved as prog4b.py
'''

# Asking For The Integers/Variables
print('')
print('')
x = int(input('First Number (Positive Integer Only): '))
y = int(input('Second Number (Positive Integer Only): '))
rem = int(x%y)
quotient = float(x/y)

# Outputs Remainder and Quotient of The Two Integers
print('')
print('')
print('Remainder: ', rem)
print('Quotient: ', quotient)