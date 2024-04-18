import math
def volume(r, h):
    vol=math.pi*r**2*h
    return vol

radius = float(input('Enter radius: '))
height = float(input('Enter height: '))
print('Volume of cylinder is:', round(volume(radius,height),2))
