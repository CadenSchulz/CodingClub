'''
Created on Mon Feb 9 3:16:05 2022

@author: C. Schulz

Description: Computing whether or not two inputted characters are the same.

Saved as prog5a.py
'''

# Variables/Asking For Characters
letter1 = input('First Character (Letter): ')
letter2 = input('Second Character (Letter): ')
length1 = len(letter1)
length2 = len(letter2)
if length1 >= 2:
    print('Please type two individual characters only.')
    quit()
if length2 >= 2:
    print('Please type two individual characters only.')
    quit()

# Computing Whether or Not The Two Strings Are The Same
elif letter1 == letter2:
    print('The Two Characters ARE The Same.')
else:
    print('The Two Characters ARE NOT The Same.')