'''
Created on Wed Mar 2 10:42:01 2022

@author: C. Schulz

Description: 

Saved as prog8b.py
'''

def isEven(num):
    if num % 2 == 1:
        return 'odd'
    else:
        return 'even'

num = int(input('Enter A Number: '))

result = isEven(num)
print(f'{num} is {result}.')