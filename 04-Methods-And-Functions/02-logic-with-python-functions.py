def even_check(number):
    return number % 2 == 0


print(even_check(20))
print(even_check(5))


def check_some_even(num_list):
    '''
    This function returns TRUE if any of the
    numbers in list is even.
    '''
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False


print('Check some even: ', check_some_even([1, 3, 5, 6, 7]))
print('Check some even: ', check_some_even([1, 3, 5, 7]))


def return_even_numbers(num_list):
    '''
    This function returns all even numbers in the list.
    '''
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers


print('Get even numbers: ', return_even_numbers([1, 3, 5, 6, 7]))
print('Get even numbers: ', return_even_numbers([1, 3, 5, 7]))
