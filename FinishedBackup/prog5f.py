'''
Created on Mon Feb 11 11:43:06 2022

@author: C. Schulz

Description: Using a name and two integers to collect information

Saved as prog5f.py
'''

    # Imports/Math Import
import math as math
import random

    # Variables/Asking for name and numbers
name = input('Your Name: ')
num1 = int(input('FIRST Number: '))
if num1== 0:
    print('Enter Another Number Other Than 0!')
    quit()
num2 = int(input('SECOND Number: '))
if num1== 0:
    print('Enter Another Number Other Than 0!')
    quit()

    # Name Length Variable
length = len(name)

    # Product and Quotient Variables
product = int(num1*num2)
quotient = float(num1/num2)

    # Reciprocal Variable
reciprocal = float(1/num1)


    # Powers and Nth Root Variables
power = pow(num1, num2)
nthRoot = num1**(1/float(num2))
fifthPower = num1**5
    
    
    
    # Fibonacci Sequence Variables
fib1 = num1 + num2
fib2 = num2 + fib1
fib3 = fib1 + fib2

    # Pi and e Variables
pi = math.pi
e = math.e

    # Making A Cleaner Looking Output
print('\n')

    # Length of Name
print('Your name is', length, 'characters long!')

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
if num1 or num2 == 0:
    print(f'Reciprocal of {num1} does not exist!')
else:
    print("{} {:.3f}".format('FIRST Number\'s Reciprocal: ', reciprocal))

    # Value of The First Number Raised To The Second Number
print('The FIRST Number ^ SECOND Number =', power)

    # The First Number Being Rooted From The Second Number
print('The', num1, 'root of', num2,'=', nthRoot)

    # The Value of The First Number To The Fifth Power
print(num1, 'to the 5th power =', fifthPower)

    # Common Log of The First Number
if num1 < 0:
    print(f'The Common Log of {num1} does not exist!')
else:
    commonLog = math.log10(num1)
    print('The Common Log of', num1, '=', commonLog)

    # Natural Log of The Second Number
if num2 < 0:
    print(f'The Natural Log of {num2} does not exist!')
else:
    naturalLog = math.log(num2)
    print('The Natural Log of', num2, '=', naturalLog)

    # Fibonacci Sequence
print('Fibonacci Sequence Starting With the FIRST Number=', num1, num2, fib1, fib2, fib3)

    # Random Number 0-1
print("{} {:.3f}".format('Random Number (0-1):', random.uniform(0, 1)))

    # Value of Pi
print('The Value of "pi" =', pi)

    # Value of e
print('The Value of "e" =', e)

    # Determining Which Number is Bigger (FIRST or SECOND)
while True:
    if num1 > num2:
        print(f'Your FIRST number, {num1}, is larger than your SECOND number, {num2}.')
        break
    elif num2 > num1:
        print(f'Your SECOND number, {num2}, is larger than your FIRST number, {num1}.')
        break
    elif num1 == num2:
        print(f'The Two Numbers You Inputted ({num1},{num2}) Are The Same!')
        break