'''
Created on Thurs Feb 24 3:35:29 2022

@author: C. Schulz

Description: Printing The Multiples Of An Inputted Number

Saved as prog7b.py
'''
    # Asking user for a number
ask = int(input('Your number: '))
    # Printing numbers 0-500 while skipping the user's preffered number (stepping)
for x in range(0,500,ask):
    print(x)