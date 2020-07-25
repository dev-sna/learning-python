# Immutability
name = 'Sam'
# Wrong code
# name[0] = 'P'

last_letters = name[1:]
print('last_letters', last_letters)

print('concat: ', 'P' + last_letters)

# Repeat
letter = 'z'
print('repeated: ', letter*10)

# Some method
print(name.upper())  # SAM
print('crap'.capitalize())  # Crap
print('some crap to test split'.split('s'))
# ['', 'ome crap to te', 't ', 'plit']

# ---- Print formatting ----
print('The is an {} string'.format('INSERTED'))
# Indices
print('This {2} {1} {0}.'.format('crap', 'all', 'is'))
# Keywords
print('This {i} {a} {c}.'.format(c='crap', a='all', i='is'))
# Float formatting
result = 100/777
print(result)
print('The results is {}'.format(result))  # could be (r=result) too
# {r: width.precision f}
print('The results with precision is {r:1.3f}'.format(r=result))

# f-string or formatted string literal(new python 3.6)
name = "Jose"
print(f'Hello his name is {name}')
