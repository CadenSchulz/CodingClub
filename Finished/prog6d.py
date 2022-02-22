'''
Created on Thurs Feb 17 3:56:14 2022

@author: C. Schulz

Description: Counting 1-5000 in 5 separate columns

Saved as prog6d.py
'''

    # Variables/List Of Numbers In A Range
rows = list(range(1,5001))
number = 0

    # Printing Numbers In 5 Separate Rows
while number < 5000:
    print("{:20d}".format(rows[number]), end = ' ')
    number += 1
    if number % 5 == 0:
        print('\n')