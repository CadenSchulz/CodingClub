'''
Created on Mon Feb 2 10:54:32 2022
@author: C. Schulz
Description: Dividing positive integers and finding the quotient/remainder
Saved as prog4b.py
'''

from math import remainder
from turtle import right

print('')
print('')
x = int(input('First Number (Positive Integer Only): '))
y = int(input('Second Number (Positive Integer Only): '))

rem = int(x%y)
quotient = float(x/y)


print('')
print('')
print('Remainder: ', rem)
print('Quotient: ', quotient)