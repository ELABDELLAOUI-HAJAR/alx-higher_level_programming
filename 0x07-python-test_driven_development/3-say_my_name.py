#!/usr/bin/python3
"""Define a function say_my_name"""


def say_my_name(first_name, last_name=""):
    """
    Definition of say_my_name

    args:
        first_name required
        last_name Optional by default ""
    Return:
        My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
