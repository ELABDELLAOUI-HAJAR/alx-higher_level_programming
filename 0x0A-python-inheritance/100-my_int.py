#!/usr/bin/python3
"""Define MyInt class that inherite from int"""


class MyInt(int):
    """Definition of MyInt class
        that inherite from int
    """

    def __eq__(self, other):
        """evaluate == comparaison"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """evaluate != comparaison"""
        return int.__eq__(self, other)
