#types of iterables
stri_i = 'string'
list = [1,2,3,4]
tuple = ('allspice','bay','cinnamon','dandelion')
dict1 = {'1':'allspice' ,'2':'bay' ,'3':'cinnamon' ,'4':'dandelion'}
range_5 = range(1,7)

counter = 0
spices = []

#while counter == 0:
#    for x == tuple:






for x in tuple:
    counter += 1
    if x == 'bay'or x == 'dandelion':
        print('Bay is a leaf')
    else :
        spices.append(x) 
        print(f'{x.capitalize()} is a spice')

print(x)

print(f'We have {counter} items in our \n spice cabinet')
print(f'{spices} are spices')
