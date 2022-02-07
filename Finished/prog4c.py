'''
Created on Mon Feb 2 10:54:32 2022

@author: C. Schulz

Description: Telling whether a number is factor of another

Saved as prog4c.py
'''

from time import sleep


x = int(input('First Number (Positive Integer): '))
sleep (0.5)                                                         # For Cleaner Formatting
y = int(input('Second Number (Positive Integer): '))


ans = y//x
rem = y%x

if ans == 0 or rem >0:
    sleep(0.5)                                                      # For Cleaner Formatting
    print('These two integers ARE NOT factors of each other.')
    sleep(0.5)                                                      # For Cleaner Formatting
else:
    sleep(0.5)                                                      # For Cleaner Formatting
    print('These two integers ARE factors of each other.')
    sleep(0.5)                                                      # For Cleaner Formatting