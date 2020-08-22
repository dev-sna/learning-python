# Key: value pairs
# Unordered and can't be sorted
# New key:value pairs are inserted wherever it finds efficient

person_info = {'name': 'James', 'age': 2}
# access a property
print('Name: ', person_info['name'])

diverse_key = {'key': 1, 'list': [1, 2, 'a'], 'dict': person_info}
print('Dict: ', diverse_key['dict'])
print('Operation on prop: ', diverse_key['list'][2].upper())

# add a new key:value pair
diverse_key['new'] = 'new value'
print('With new prop', diverse_key)
