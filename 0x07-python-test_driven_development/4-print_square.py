#!/usr/bin/python3
"""Define a print_square function"""


def print_square(size):
    """
    Definition of print_square function.

    Args:
        size : is the size length of the square
    Exceptions:
        when size is not integer: TypeError with
        msg 'size must be an integer'

        when size < 0: TypeError with msg :
        'size must be >= 0'
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise TypeError('size must be >= 0')

    for i in range(0, size):
        [print("#", end="") for x in range(0, size)]
        print()
