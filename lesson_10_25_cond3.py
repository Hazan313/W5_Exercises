# Boolean operators
# recycling input
cans = 1
bottles = 0
boxes = 1


#print(cans < bottles and bottles < 5) # And is Both conditions must be true
#print(cans < bottles or bottles < 5) 

if (cans > 0 or bottles > 0) or not boxes > 0:
    print('Call the recycling service for pickup.')
elif boxes != 0:
    print("We've gotta do something with these boxes.")
    
# print('They\'ll tell you "Call us for pickup"') # \ refers to escape character notation to use quotes,commas in quotes without errors

# MATCH CASE

greeting = input('Enter your greeting:')

match greeting:
    case 'Hello' :
         print('Hello to you too!')
    case 'Good morning' :
        print('Good morning to you to!')
    case other: 
        print('Oh you don\'t say?')     

if greeting == 'Hello':
    print("Hello to you to!")
elif greeting== 'Good morning':
    print('Good morning to you too!')
else: 
    print('Oh you don\'t say?')