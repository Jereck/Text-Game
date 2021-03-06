import random

def weighted_random_selection(obj1, obj2):
    weighted_list = 3 * [id(obj1)] + 7 * [id(obj2)]
    selection = random.choice(weighted_list)

    if selection == id(obj1):
        return obj1

    return obj2


def print_bold(msg, end='\n'):
    """Print a string in 'bold' font"""
    print(msg, end=end)
