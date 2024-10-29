# List all variables:

#1
address_dict = {'Name' : 'Rob',
                'Address' : '14 Grunger Ave',
                'City' : 'Pretoria',
                'State' : 'Vereenining',
                'Zip' : 21953.346}

First_name = {'First name' : 'Ronald'}
Last_name = {'Last name' : "Weasley"}
full_name = (f'{First_name['First name']} {Last_name['Last name']} ') # Created and added 2 dictionary key:value pairs to a tuple, to then add the tuple to another dictionary   

# Formulate all processing:

#4
address_dict['Name']=full_name

#5
address_dict.update({'honorific' : 'Dr'})

#3
# address_dict.pop('Name')
# del address_dict['Name']

# Print all results:

#2
print(f"{(address_dict['Name'])} \n{(address_dict['Address'])} \n{(address_dict['City'])} 
      \n{(address_dict['State'])} \n{(address_dict['Zip'])}") 
#6

print(f"{address_dict['honorific']} {(address_dict['Name'])} \n{(address_dict['Address'])} 
      \n{(address_dict['City'])} \n{(address_dict['State'])} \n{(address_dict['Zip'])}")