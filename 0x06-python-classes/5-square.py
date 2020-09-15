#!/usr/bin/python3
"""
dsf
"""
class Square:
    """
    sdf
    """
    def __init__(self, size=0):
        self.__size = size

    # Property
    @property
    def size(self):
        """
        dsfs
        """
        return self.__size

    # Setter modifies
    @size.setter
    def size(self, value):
        """
        dsfsd
        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """
        dsfds
        """
        return self.__size ** 2

    def my_print(self):
        """
        dsfs
        """
        size = self.__size

        if size == 0:
            print()

        for row in range(size):
            print('#' * size)
