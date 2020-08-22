my_numbers_list = [1, 2, 3]
my_mixed_list = ['a', 1, 1.5]

print(my_numbers_list[1:])

# concatenate
concatenated = my_numbers_list + my_mixed_list
print(concatenated)

# mutate
concatenated[4] = 4
print(concatenated)

# append
my_numbers_list.append(4)

# pop
popped_item = my_mixed_list.pop()
print('popped: ', popped_item)
print('my_mixed_list', my_mixed_list)

# pop at index
popped_item = my_numbers_list.pop(1)
print('popped indexed: ', popped_item)
print('my_numbers_list: ', my_numbers_list)

# sort
num_list = [1, 3, 1, 2, 7, 5, 6, 4]
num_list.sort()
print('num_list: ', num_list)
