'''
Created on Thurs Feb 24 5:42:31 2022

@author: C. Schulz

Description: Multiplication table ranging with 2 inputted numbers

Saved as prog7f.py
'''
    # Variables/Asking User For Two Numbers
num1 = int(input('First Number: '))
num2 = int(input('Second Number: '))
    # Making The Inputted Number Increase 1 For The Range To Work Properly
num3 = num2 + 1

    # Printing The Top Row Of Numbers In The Range
print('\n', end = '\t')
for x in range(num1, num3):
    print(end = "{:>9d}".format(x))
print('\n')
    # Printing The First Column Vertically Of The Range
for y in range(num1, num3):
    print(y, end = '\t')
        # Printing The Multiplication Numbers Across The Rows And In The Correct Column
    for z in range(num1, num3):
        print(end = "{:>9d}".format(y*z))
    print()