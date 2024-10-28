#Pet store calculator

# define the known
num_cats=6
cat_food = {'from': 10, 'purina': 30, 'kirkland': input('How much Kirkland cat food in inventory?')}
cat_serving = 0.10

print(f'Number of cats : {num_cats}')
print(f'Cat food in stock: {cat_food}')

#calcualte the unknown
if cat_food['kirkland'] > 0:
        cat_food['kirkland'] = cat_food['kirkland'] - (num_cats * cat_serving)

elif cat_food ['from'] > 0:
        cat_food['from'] = cat_food['from'] - (num_cats * cat_serving)


else:
        cat_food['purina'] = cat_food['purina'] - (num_cats * cat_serving)


print(f'After feeding the cats : {cat_food}')