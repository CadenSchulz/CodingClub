'''
Created on Thurs Mar 2 10:49:07 2022

@author: C. Schulz

Description: Telling whether an integer is even or odd

Saved as prog8e.py
'''

    # Defining a function named isEven/Finding the remainder of a number to tell whether it is odd or even
def isEven(num):
    if num % 2 == 1:
        return 'odd'
    else:
        return 'even'

    # Asking the user for a number
num = int(input('Enter A Number: '))

    # Calling the function
print(f'{num} is {isEven(num)}.')