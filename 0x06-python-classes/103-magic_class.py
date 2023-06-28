#!/usr/bin/python3
"""Define MagicClass class"""

import math


class MagicClass:
    """Definition of MagicClass"""

    def __init__(self, radius=0):
        """function to initialise MAgicClass fields"""
        self.__radius = 0
        if (type(radius) is not int and
                type(radius) is not float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """return the area of a circle"""
        return self.__radius**2 * math.pi

    def circumference(self):
        """return circumference of a circle"""
        return 2 * math.pi * self.__radius
