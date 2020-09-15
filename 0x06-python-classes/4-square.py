#!/usr/bin/python3
"""
dsfs
"""
class Square:
"""
dfsf
"""
    def __init__(self, size=0):
    """
    dsffds
    """
        self.__size = size

    # Property
    @property
    def size(self):
    """
    dfsfds
    """
        return self.__size

    # Setter modifies
    @size.setter
    def size(self, value):
    """
    sdfs
    """
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
    """
    dsfdsf
    """
        return self.__size ** 2
