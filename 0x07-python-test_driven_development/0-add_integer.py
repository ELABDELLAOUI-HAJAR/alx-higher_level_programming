#!/usr/bin/python3
# 0-add_integer.py
# HAJAR EL ABDELLAOUI
'''Define one function add_integer'''


def add_integer(a, b=98):
    '''Definition of add_integer function

    args: 2 integers or floats
    if a and b are not integers or floats we raise TypeError
    exception with the message: a must be an integer or
    b must be an integer

    Return: an integer that represent the addition of a and b
    '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
