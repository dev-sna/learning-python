# Function names are in snake cases
def greet_a_person(name='Default'):
    '''
    Docstring explains a function
    '''
    print(f'Hello {name}')


greet_a_person('Jake')


def add_num(num1, num2):
    return num1+num2


addResults = add_num(2, 3)
print('Add result: ', addResults)
