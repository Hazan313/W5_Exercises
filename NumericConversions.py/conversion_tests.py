#   Description:  This script tests various numeric conversion techniques
#   Author: Hassan Zaidi

#   list the variables:

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

#   Formulate the processing:

#   Instructions:
#   Cast as integer using int()
#   Cast as float using float()
#   For variable a, try casting into a float then integer, like this: int(float(a))

#   Use slicing to add just the numeric portion of the string to a new variable
#   (remember, indexing always starts with 0!), and cast the number as an integer or
#   string, whichever is appropriate

#   For variables a and d, use the .strip() method to remove the leading/trailing
#   spaces.

#   Variable explanation:
#   (var)(i), i stands for integer
#   (var)(f), f stands for float
#   (var)(s), s stands for sliced string/var
#   (var)(r), r stands for removing leading/trailing spaces 


#   ai = int(a)
bi = int(b)
#   ci = int(c)
#   di = int(d)
#   af = float(a)
bf = float(b)
#   cf = float(c)
#   df = float(d)
af = int(float(a))
aofs = a[1:6] # 'as' is already recognized as another operator
bs = b[0:2]
cs = c[0:3]
ds = d[-2:-1]
ar = a.split()
dr = d.split() 

#   Print the output:

#   print(ai, type(ai)) # error code: ValueError: invalid literal for int() with base 10: ' 101.1 '
print(bi, type(bi)) # No error code givens
#   print(ci,type(ci)) #error code: ValueError: invalid literal for int() with base 10: '402 Stevens'
#   print(di,type(di)) #error code: ValueError: invalid literal for int() with base 10: 'Number 5 '
print(af, type(af)) # No error code given
print(bf, type(bf)) # No error code given
#   print(cf, type(cf)) #error code given: ValueError: could not convert string to float: '402 Stevens'
#   print(df, type(df)) #error code given: ValueError: could not convert string to float: 'Number 5 '
print(af, type (af)) 
print(f'{len(a)} \n {len(b)} \n {len(c)} \n {len(d)}')
print(aofs, type (aofs))
print(bs,type (bs))
print(cs, type(cs))
print(ds, type(ds))
print(ar)
print(dr)