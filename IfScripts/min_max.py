#   Exercise 4b Lab4:
#   Create a script named min_max.py that displays both the smallest and then the
#   largest of three numbers.

#   Name your variables a, b, and c and assign them values. Then use if/else statements
#   to determine and display the answer.

#   Be sure to test your script using an assortment of different values in your variables, so
#   that you look at a variety of different number combinations


# List all varaibles:
import random

a =  random.randint(-100000000000000,100000000000000)
b =  random.randint(-100000000000000,100000000000000)
c =  random.randint(-100000000000000,10000000000000)
min = 'min'   #smallest number of the bunch
max = 'max'   #largest number of the bunch

# Formualate all processess:
if a > b and a > c :
    print(f"{a} is biggest number.")
elif a< b and a < c :
    print(f"{a} is the smallest number.")
elif b < a < c:
    print(f"{a} is neither the biggest nor the smallest number.")
elif c < a < b:
    print(f"{a} is neither the biggest nor the smallest number.")

if b > a and b > c :
    print(f"{b} is the biggest number.")
elif b < a and b < c :
    print(f"{b} is the smallest number")
elif a < b < c:
    print(f"{b} is neither the biggest nor the smallest number.")
elif c < b < a :
    print(f"{b} is neither the biggest nor the smallest number.")

if c > a and c > b:
    print(f'{c} is the biggest number.')
elif c < a and c < b :
    print(f"{c} is the smallest number.")
elif a < c < b:
    print(f'{c} is neither the biggest nor the smallest number')
elif b < c < a:
    print(f"{c} is neither the biggest nor the smallest number.")

# Print all results: