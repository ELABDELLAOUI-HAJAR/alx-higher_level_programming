#!/usr/bin/python3
"""Define Base class"""


class Base:
    """Definition of Base class

    class attributes:
        nb_objects: nbr of instances
    instance atrributes:
        id: Base identifier
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
