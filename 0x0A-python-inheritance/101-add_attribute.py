#!/usr/bin/python3
"""Define a function add_attribute"""


def add_attribute(obj, name, value):
    """Definition of add_attribute function that adds
        a new attribute to an object

        Args:
            obj: the object
            name: the attribute name
            value: the attribute value
        Exceptions:
            TypeError: when the attribute can't be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
