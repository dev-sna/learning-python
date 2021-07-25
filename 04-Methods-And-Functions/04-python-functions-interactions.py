from random import shuffle

example = [1, 2, 3, 4, 5]
# It doesn't return. It mutates.
shuffle(example)

print("Shuffled: ", example)


# Game
my_list = ["", "O", ""]


def shuffle_list(my_list):
    shuffle(my_list)
    return my_list


shuffled_list = shuffle_list(my_list)


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Please enter 0, 1 or 2: ")
    return int(guess)


guess = player_guess()


def check_guess(shuffled_list, guess):
    if my_list[guess] == 'O':
        print("Correct")
    else:
        print("Wrong guess!")
        print(shuffled_list)


check_guess(shuffled_list, guess)
