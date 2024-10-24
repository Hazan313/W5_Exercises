# Area of circle  A=πr2
# A=(π)r^2 

import math

radius = 9
pi = 3.1415926535  # (Source: https://calculat.io/en/number/first-digits-of-pi/10)
Area = ((pi) * int(int(radius) * int(radius)))
Area = round(Area, 2)

print('The area of a circle with radius ' + str(radius) + ' is ' + str(Area) + 'mm^2')

