import math
def Formula(radius):
    pi = math.pi
    diameter = radius**2
    area = pi*diameter
    return area

radius = float(input('Radius Value: '))

answer = Formula(radius)
print("{}{:.4f}".format('Area Of The Circle: ', answer))