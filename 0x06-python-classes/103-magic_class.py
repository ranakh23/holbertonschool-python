#!/usr/bin/python3
"""
dsfsdf
"""


import math

# fdjhfsdj
class MagicClass:
    # dsfksdfkj
    def __init__(self, radius):
        # dfjksdkfj
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self, radius):
        # dsfkajkj
        return self.__radius ** 2 * math.pi

    def circumference(self, radius):
        # adsfjhjh
        return 2 * math.pi * self.__radius
