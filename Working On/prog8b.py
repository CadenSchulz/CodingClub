'''
Created on Tues Mar 8 10:22:00 2022

@author: C. Schulz

Description: Computing factorials of integers

Saved as prog8b.py
'''

def Factorial(n):
    if n<0:
        print(-1)
    elif n >= 0:
        x = 1
        for y in range (1, n + 1):
            x = x*y
    return x

q1 = int(input('Enter Number: '))

answer = Factorial(q1)
print(f'The factorial of {q1} is {answer}.')