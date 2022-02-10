'''
Created on Mon Feb 9 11:34:58 2022

@author: C. Schulz

Description: Computing the greatest common divisor of two integers

Saved as prog5d.py
'''
# Imports
import math

# Variables/Asking for two integers
num1 = int(input('FIRST Number: '))
num2 = int(input('SECOND Number: '))

# Computing the GCD of the two integers
print ('The gcd of', num1, 'and', num2, 'is: ')
print (math.gcd(num1,num2))