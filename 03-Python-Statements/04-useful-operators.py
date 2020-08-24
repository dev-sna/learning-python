# Importing
from random import shuffle, randint

# range(start,upto,step)
for num in range(3, 10, 2):
    print(num)

generatedList = list(range(0, 11, 2))
print('Generated list: ', generatedList)

# Enumerate
for item in enumerate('abcde'):
    print(item)  # gives a tuple e.g. (0,'a')

# zip
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
merged_lists_address = zip(list_1, list_2)
print('Merged lists: ', merged_lists_address)  # only gives a memory location
# to iterate zipped lists
for _ in merged_lists_address:
    print(_)  # gives tuples
# can be caste to list
merged_lists = list(merged_lists_address)

# in
print(1 in [1, 2, 3])
print('a' in 'camel')
print('name' in {'name': 'Jack'})
print('Jack' in {'name': 'Jack'}.values())

# min, max
min_num = min([1, 2, 3, 4])
max_num = max([1, 2, 3, 4])

# shuffle (it doesn't return)
list_to_shuffle = [1, 2, 3, 4, 5, 6, 7, 8]
shuffle(list_to_shuffle)
print('Shuffled list: ', list_to_shuffle)

# random integer
random_int = randint(0, 100)
print('Random integer: ', random_int)

# User input
# Input is always a string. We need to parse it if we
# need a number.
name = input('Enter your name: ')
print(f'Your name is {name}')
