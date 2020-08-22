# Tuples are same as lists but, they're immutable.
# We use parenthesis to construct a tuple.
# It's used for data integrity.

my_tuple = (1, 2, 3, 'A', 'A', 'b')
my_list = [1, 2, 3]

print('First element: ', my_tuple[0])
print('Total appearance of A: ', my_tuple.count('A'))
print('First appearance of A: ', my_tuple.index('A'))

my_list[0] = 'NEW'
# throws error
# my_tuple[0] = 'NEW'
