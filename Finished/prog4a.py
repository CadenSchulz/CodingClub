'''
Created on Mon Feb 2 10:54:32 2022

@author: C. Schulz

Description: Computing commission of a salesperson

Saved as prog4a.py
'''

# Imports
from time import sleep

# Variables/Getting Commission Information
sale = float(input('Montly Sales ($): '))
commission = float(sale * 0.2)


# Cleaner Output Aesthetic
print('.')
sleep(0.5)
print('.')
sleep(0.5)
print('____________')
sleep(0.5)


# Code/Calculating Commission of Salesperson
print("{} {:.2f}".format('Monthly Sales ($): ', float(sale)))
sleep(0.5) #For Cleaner Formatting
print("{} {:.2f}".format('Commission Earned ($): ', float(commission)))

# Cleaner Output Aesthetic
print('____________')
sleep(0.5)
print('.')
sleep(0.5)
print('.')
sleep(0.5)