'''
Created on Mon Feb 4 10:39:37 2022

@author: C. Schulz

Description: Using a numeric grading scale to tell a user's grade.

Saved as prog4d.py
'''



# Imports/Functions
from time import sleep
# Imports/Functions



# Cleaner Formatting
print('.')            
sleep(0.5)            
print('.')            
sleep(0.5)            
print('.')            
sleep(0.5)            
# Cleaner Formatting



grade = float(input('Current Class Grade: '))



# Cleaner Formatting
print('.')            
sleep(0.5)            
print('.')            
sleep(0.5)            
print('.')            
sleep(0.5)            
# Cleaner Formatting



if grade > 89.5 and grade <= 100:
    print('Your current grade is an "A" ')

if grade >= 79.5 and grade <= 89.49:
    sleep (0.5) # For Cleaner Formatting
    print('Your current grade is an "B" ')
    
if grade >= 69.5 and grade <= 79.49:
    sleep (0.5) # For Cleaner Formatting
    print('Your current grade is an "C" ')

if grade >= 59.5 and grade <= 69.49:
    sleep (0.5) # For Cleaner Formatting
    print('Your current grade is an "D" ')
    
if grade >= 0 and grade <= 59.49:
    sleep (0.5) # For Cleaner Formatting
    print('Your current grade is an "F" ')
    
if grade > 100:
    sleep (0.5) # For Cleaner Formatting
    print('Your grade can\'t be over 100! Please start over.'),
    quit()
if grade < 0:
    sleep (0.5) # For Cleaner Formatting
    print('Your grade can\'t be under 0! Please start over.')