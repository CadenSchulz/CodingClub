'''
Created on Mon Feb 21 8:07:22 2022

@author: C. Schulz

Description: Printing a pattern P2

Saved as prog6g2.py
'''

    # Variables/Defining The Pattern
a = '*'
b = '**'
c = '***'
d = '****'
e = '*****'
f = '******'
x = 1

    # Asking Which Way The Pattern Should Look
print('\n')
print('How Do You Want The Pattern To Look?')

    # Printing The Pattern
while True:
    q1 = input('Infinite or Singular: ')
        # Printing The Pattern Infinitely
    if q1.lower() == 'infinite':
        while True:
            print(a)
            print(b)
            print(c)
            print(d)
            print(e)
            print(f)
            continue
        # Printing The Pattern One Single Time
    elif q1.lower() == 'singular':
        while x <= 1:
            print(a)
            print(b)
            print(c)
            print(d)
            print(e)
            print(f)
            x += 1
        break
        # Starting The Code Over If User Enters Something Other Than "Infinite" or "Singular"
    else:
        print('Not An Option.')
        continue