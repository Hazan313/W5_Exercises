# List all variables:
import time
import random

ct = random.randint(0,23)  #current time # Time input treated as full 24 hour clock, not 12 am/pm
#ct = 29
 
# Formulate all processes:

if ct >= 24 :
    print(f'Invalid Time input! Please check code!')
elif ct == 23 or ct <= 4:
    print(f"What are you doing up so late?") 
elif ct <= 10 :
    print(f'Good morning!')
elif 10 < ct < 17:
    print(f"Good day!")
    #print(f'The time is {ct}.00')
elif 17 < ct < 24:
    print(f"Good evening!")



if ct <= 11 :
    print(f'The time is {ct}.00 and it is before midday')
elif ct > 11 :
    print(f'The time is {ct}.00 and it is after midday')


# Print all results: