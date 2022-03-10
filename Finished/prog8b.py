'''
Created on Tues Mar 8 10:22:00 2022

@author: C. Schulz

Description: Computing factorials of integers

Saved as prog8b.py
'''
    # Defining a function named Factorial/Multiplying the number by the next after the previous
def Factorial(n):
    if n<0:
        print(-1)
    elif n >= 0:
        x = 1
        for y in range (1, n + 1):
            x = x*y
    return x

    # Asking user for a number
q1 = int(input('Enter Number: '))

    # Printing the output/Calling the function
print(f'The factorial of {q1} is {Factorial(q1)}.')