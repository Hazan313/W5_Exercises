# /* You are going to tile a room whose dimensions are length by width feet. There are
# twelve tiles per box, each 1 foot by 1 foot. How many boxes of tiles do you need? You
# can only buy full boxes, not a partial box.
# 
# You also want to buy 10% more tiles than you need in order to handle chips, breakage,
# and mess-ups. How many total boxes will you buy? */
import math
lengthr = 24
widthr = 18
rarea = lengthr * widthr
tpb = 12
boxneeded= rarea/tpb
print(f'{boxneeded}ft^2 is the area.')
boxneeded2  = ((0.1 * boxneeded) + boxneeded)

print(f'The amount of boxes needed are {math.ceil(boxneeded2)}.')