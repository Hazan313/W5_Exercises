# How do you calculate the distance between coordinates (x1,y1) and (x2,y2)?
import math
# 

# Define the number
x1 =2
y1 =3
x2 =-2
y2 =-4
DCF = (((x2 -x1)*(x2-x1)) + ((y2-y1) * (y2-y1)))
# Distance Coordinates Final

# Calculate the square root
Distance = math.sqrt(DCF)

# Print the result
print(f'Distance between these two co-ordinates:({x1},{y1}) and ({x2},{y2}), are {Distance:.2f}')

# Ask Bess if theres a square function and how to fix this error : print( f"The distance between the coordinates " + (x1,y1) 'and ' + (x2,y2) + 'is ' + round(Distance,2) )
#                                                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
