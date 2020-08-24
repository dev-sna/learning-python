# Unique way of quickly creating a list.
myString = 'hello'
myList = [letter for letter in myString]
print('Created list: ', myList)

# with range
num_list = [num for num in range(0, 11)]
print('Num list: ', num_list)

# even numbers
num_list = [num for num in range(0, 11) if num % 2 == 0]
print('Even list: ', num_list)

# squared numbers
num_list = [num**2 for num in range(0, 11) if num % 2 == 0]
print('Squared even list: ', num_list)

# if, else: order is changed
num_list = [x if x % 2 == 0 else x**2 for x in range(1, 11)]
print('Even Odd(squared) list: ', num_list)

# nested for loops
multiplication_list = [x*y for x in [1, 2, 3] for y in [1, 10, 100]]
print('Multiplication list: ', multiplication_list)
