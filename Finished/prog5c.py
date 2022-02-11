'''
Created on Mon Feb 9 11:22:07 2022

@author: C. Schulz

Description: Determining which inputted integer is larger

Saved as prog5c.py
'''
# Variables/Asking for integers
num1 = input('FIRST Number: ')
num2 = input('SECOND Number: ')

# Computing which number is larger
if num1 > num2:
    print('Your FIRST number,', num1 + ', is larger than your SECOND number,', num2 + '.')
    quit()
elif num2 > num1:
    print('Your SECOND number,', num2 + ', is larger than your FIRST number,', num1 + '.')
    quit()
elif num1 == num2:
    print(f'The Two Numbers You Inputted ({num1},{num2}) Are The Same!')