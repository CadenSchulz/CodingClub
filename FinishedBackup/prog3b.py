'''
Created on Mon Feb 1 5:49:41 2022
@author: C. Schulz
Description: Calculating miles per gallon
Saved as prog3b.py
'''

from time import sleep


print('.')      # For Cleaner Formatting
sleep(0.25)     # For Cleaner Formatting
print('.')      # For Cleaner Formatting
sleep(0.25)     # For Cleaner Formatting
print('.')      # For Cleaner Formatting
sleep(0.25)     # For Cleaner Formatting



miles = float(input('Miles Driven: '))
gas = float(input('Gas Used: '))
milesPerGallon = miles / gas


print('.')                                                        # For Cleaner Formatting
sleep(0.25)                                                       # For Cleaner Formatting
print('.')                                                        # For Cleaner Formatting
sleep(0.25)                                                       # For Cleaner Formatting
print('_______________________________________________________')  # For Cleaner Formatting
sleep(0.25)                                                       # For Cleaner Formatting


print("{:20s} {:20s} {:20s}".format('MILES'.center(15), 'GAS'.center(15), 'MILES PER'.center(15)))
print("{:20s} {:20s} {:20s}".format('DRIVEN'.center(15), 'USED'.center(15), 'GALLON'.center(11)))
print("{:20s} {:20s} {:20s}".format('------'.center(15), '----'.center(15), '---------'.center(15)))

print("{:^14d} {:^28d} {:^12.3f}".format(int(miles), int(gas), float(milesPerGallon)))


print('_______________________________________________________')  # For cleaner formatting
sleep(0.25)                                                       # For cleaner formatting
print('.')                                                        # For cleaner formatting
sleep(0.25)                                                       # For cleaner formatting
print('.')                                                        # For cleaner formatting
sleep(0.25)                                                       # For cleaner formatting