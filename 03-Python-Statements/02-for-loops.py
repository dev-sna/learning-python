my_list = [1, 2, 3, 4, 5]

for num in my_list:
    print('Number is: ', num)

for num in my_list:
    if num % 2 == 0:
        print(f'{num} is even.')
    else:
        print(f'{num} is odd.')

list_sum = 0
for num in my_list:
    list_sum += num

print('Sum: ', list_sum)

# Iterating over string
for letter in 'Hello world':
    print(letter)

# Iterating over tuples
tup = (1, 2, 3)
for _ in tup:
    print('Tup item: ', _)

# Tuple unpacking
tup_list = [(1, 2), (3, 4), (5, 6)]

for a, b in tup_list:  # can also be (a,b)
    print('Individual tuple items: ', a, b)

# -------- Iterating over disctionaries --------
person = {'name': 'John', 'age': 40}
# Keys
for key in person:
    print('Dict key: ', key)
# Items
for item in person.items():
    print('Dict item: ', item)
# Items
for key, value in person.items():
    print('Key, value: ', key, value)

# Nested for loops
num_list = []
for x in [1, 2, 3]:
    for y in [1, 10, 100]:
        num_list.append(x*y)
print('Nested for lopps list: ', num_list)

# -------- break, continue and pass --------
# break: breaks the current loop
# pass: does nothing
# continue: goes to the top of current loop, skips the current iteration

my_list = [1, 2, 3, 4, 5, 6]
for _ in my_list:
    pass
print('End.')

for letter in 'craps':
    if letter == 'a':
        continue
    if letter == 'p':
        break
    else:
        print('Letter: ', letter)
