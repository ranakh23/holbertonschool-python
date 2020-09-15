#!/usr/bin/python3
"""
dfs
"""


class Square:
    """
    dsfdsf
    """
    def __init__(self, size=0):
    """
    dsfdsf
    """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
    """
    dsfdsf
    """
        size = self.__size
        return size * size
