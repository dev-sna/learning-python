# *args
def myfuncArgs(*args):
    # *args gives a tuple
    # Returns 5% of the sum of a and b
    return sum(args) * 0.05


print(myfuncArgs(40, 60, 100))

# **lwargs


def myfuncKwargs(**kwargs):
    # **kwargs gives a dict
    if 'fruit' in kwargs:
        print('My favorite fruit is: {}'.format(kwargs['fruit']))
    if 'veggie' in kwargs:
        print('My favorite veg is: {}'.format(kwargs['veggie']))
    else:
        print('No fruit found')


myfuncKwargs(fruit='Mango', veggie='lettuce')
