'''
Created on Wed Mar 2 10:42:01 2022

@author: C. Schulz

Description: Calculating the sum of digits in a number

Saved as prog8d.py
'''

    # Asking user for a number
num = input('Enter Number: ')

    # Defining a function named SumOfDigits/Adding the digits
def SumOfDigits(num):
    num2 = 0
    for digit in str(num):
        num2 += int(digit)
    print(f'The Sum Of The Digits In {num} = {num2}.')
    
    # Calling the function
SumOfDigits(num)