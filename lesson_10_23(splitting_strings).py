var = 'house'

print(var[0])
print(var[0:2])

print(var[2:-1]) #up to but not including is the last number in the range #first value IS included
print(var[:-2])  
print(var[2:])

#   0   1   2   3   4 
#   H   O   U   S   E
#  -5  -4  -3  -2  -1

print(len(var))

groc_list = "milk, eggs, butter, cheese"
full_name = 'Syed Hassan Zaidi'

# print(groc_list[0:5], groc_list[5:10]) #tedious

clean_list = groc_list.split(',')
print(clean_list)
print(type(clean_list))
weird_list = groc_list.split('e')
print(weird_list) #to find the length of a string, use the len() function

print(clean_list)
item2 = clean_list[1].strip()
print(item2)
