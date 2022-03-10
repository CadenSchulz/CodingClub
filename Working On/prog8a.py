'''
Created on Tues Mar 8 10:17:22 2022

@author: C. Schulz

Description: Finding the area of a circle with the radius value

Saved as prog8a.py
'''

import math
def AreaOfCircle(radius):
    pi = math.pi
    diameter = radius**2
    area = pi*diameter
    return area

radius = float(input('Radius Value: '))

answer = AreaOfCircle(radius)
print("{}{:.4f}".format('Area Of The Circle: ', answer))