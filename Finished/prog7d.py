'''
Created on Thurs Feb 24 4:15:41 2022

@author: C. Schulz

Description: Taking an inputted number and summing 1 through that number

Saved as prog7d.py
'''

    # Ask User For Number
number = int(input("Enter Number: "))

    # Define A Sum Total
add = 0

    # Loop A Range Of The Number + 1
for x in range(number + 1):
    add = add + x
    x = x + 1
        # Prints The Numbers Added
    print(x-1)

    # Prints The Sum Of All The Numbers
print(f'The sum is {add}.')