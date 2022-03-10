'''
Created on Tues Mar 8 10:17:22 2022

@author: C. Schulz

Description: Finding the area of a circle with the radius value

Saved as prog8a.py
'''

import math

    # Defining a function/Creating variables to do the math
def AreaOfCircle(radius):
    pi = math.pi
    diameter = radius**2
    area = pi*diameter
    return area

    # Asking user for a radius value
radius = float(input('Radius Value: '))

    # Printing the area of the circle/Calling the function
print("{}{:.4f}".format('Area Of The Circle: ', AreaOfCircle(radius)))