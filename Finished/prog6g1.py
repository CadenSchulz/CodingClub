'''
Created on Mon Feb 21 12:37:52 2022

@author: C. Schulz

Description: Printing a pattern P1

Saved as prog6g1.py
'''

    # Variables/Defining The Pattern
a = '*******'
x = 1

    # Asking Which Way The Pattern Should Look
print('\n')
print('How Do You Want The Pattern To Look?')

    # Printing The Pattern
while True:
    q1 = input('Infinite, Singular, or Custom: ')
        # Printing The Pattern Infinitely
    if q1.lower() == 'infinite':
        while True:
            print(a)
            continue
        # Printing The Pattern One Single Time
    elif q1.lower() == 'singular':
        while x <= 5:
            print(a)
            x += 1
        break
    # Printing The Pattern As Many Times As The User Wants
    elif q1.lower() == 'custom':
        ask = int(input('How Many Times Do You Want The Pattern To Print? '))
        while x <= ask:
            print(a)
            x += 1
        break
        # Starting The Code Over If User Enters Something Other Than "Infinite" or "Singular"
    else:
        print('Not An Option.')
        continue