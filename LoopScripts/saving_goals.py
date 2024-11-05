#List all variables:

start_bb = 1500.38       # starting bank balance
savings_g = 13000       # savings goal
weekly_sa = 262.5         # weekly saving amount
weekly_count = 0         # weekky counter for how many weeks have passed to meet savings goal.

#Formulate all processes:

while start_bb < savings_g:
     weekly_count += 1
     start_bb = start_bb + weekly_sa
     print (f'This week my balance has increased to ${round((start_bb),2)}!')
     print(f'This is week {round((weekly_count),2)} of my savings journey!')   
     if  start_bb >= savings_g :
          break
     print(f'Goal met! My current balance is ${round((start_bb),2)}') 

print(f'In {weekly_count} weeks (or {format((weekly_count / 4), '.1f')} months), I saved ${weekly_sa} per week until I finally saved up to ${start_bb}')

#print all results:
