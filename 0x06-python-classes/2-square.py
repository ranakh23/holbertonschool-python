#!/usr/bin/python3
"""
dfsjh
"""


class Square:
    """
    dsfs
    """
    def __init__(self, size=0):
        """
        dfsdf
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
