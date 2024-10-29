# List variables:


# Formualate the processing:
#2
movies = ['Terminator', 'Cars 2','Cars 3', 'Cars ','Fast and Furious','Alien Romulus',"Transformers"]
movies.append("Jack Reacher")
movies.sort()

# Print the results:
#3
print(f'The list {('movies')} includes my top {len(movies)} favorite movies')
print(f"{movies}")
#4
print(f"{(sorted(movies))}")
print(f"{movies}")
# Notice the sorted list sorted both letters and numbers left to right.
# listname.sort() also effectively sorts the list alphabetically and numerically
# After listname.append movies amount was automatically updated. flip the append and sort order to achive all ordered results.