'''
Created on Mon Feb 11 11:43:06 2022

@author: C. Schulz

Description: Using a name and two integers to collect information

Saved as prog5e.py
'''
# Imports/Math Import
import math

# Variables/Asking for name and numbers
name = input('Your Name: ')
num1 = int(input('FIRST Number: '))
num2 = int(input('SECOND Number: '))
length = len(name)
product = int(num1*num2)
quotient = float(num1/num2)
reciprocal = float(1/num1)

# Length of Name
print('Your name is', length, 'letters long!')

# Product/Quotient of Numbers
print("{} {} {} {} {} {} {} {} {} {} {} {:.3f}".format('The PRODUCT of', num1, 'x', num2, '=', product, 'and the QUOTIENT of', num1, '/', num2, '=', quotient))

# Absolute Value
print('FIRST Number\'s Absolute Value: ', abs(num1))

# Opposite Number
if num2 > 0:
    print('SECOND Number\'s Opposite: ', -num2)
else:
    print('SECOND Number\'s Opposite: ', abs(num2))

# Reciprocal
print("{} {:.3f}".format('FIRST Number\'s Reciprocal: ', reciprocal))