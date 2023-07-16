#!/usr/bin/python3
"""Define the Square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Definition of Square class that inherits from Rectangle

    Attributes:
        id: square identifier
        size: square size
        x, y: square position
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initialise Square attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of a square"""
        return "[Square] (" + str(self.id) + ") " + str(self.x) + "/" \
            + str(self.y) + " - " + str(self.width)

    @property
    def size(self):
        """getter of the square size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of the square size"""
        self.width = value
        self.height = value
