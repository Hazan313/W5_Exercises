# Description:  This script tests various numeric
#               conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# Cast as integer using int()
# Cast as float using float()
# For variable a, try casting into a float then integer, like this: int(float(a))

# (var)(i), i stands for integer
# (var)(f), f stands for float

# ai = int(a)
# print(ai, type(ai)) # error code: ValueError: invalid literal for int() with base 10: ' 101.1 '

bi = int(b)
print(bi, type(bi)) # No error code givens

# ci = int(c)
# print(ci,type(ci)) #error code: ValueError: invalid literal for int() with base 10: '402 Stevens'

# di = int(d)
# print(di,type(di)) #error code: ValueError: invalid literal for int() with base 10: 'Number 5 '

af = float(a)
print(af, type(af)) # No error code given

bf = float(b)
print(bf, type(bf))

# cf = float(c)
# print(cf, type(cf)) #error code given: ValueError: could not convert string to float: '402 Stevens'

# df = float(d)
# print(df, type(df)) #error code given: ValueError: could not convert string to float: 'Number 5 '




