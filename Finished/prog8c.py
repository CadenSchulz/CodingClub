'''
Created on Tues Mar 8 10:46:44 2022

@author: C. Schulz

Description: Counting the number of digits in a number

Saved as prog8c.py
'''

    # Asking user for a number
n = int(input('Enter Number: '))
    
    # Setting another variable equal to the input variable
n1 = n

    # Defining a function named NumDigits/Couting the number of digits
def NumDigits(n):
    add = 0
    while(n>0):
        add += 1
        n = n//10
    print(f'The number of digits in {n1} is {add}.')
    
    # Calling the function
NumDigits(n)