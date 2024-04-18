import math
radius = float(input('Enter radius of cone: '))
height = float(input('Enter height of cone: '))
volume = (1/3)*math.pi*height*radius**2
print('Volume of the cone is',round(volume, 2))
