#!/usr/bin/python3

"""
0. Basic dictionary
"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class. Inherits from BaseCaching.
    """

    def put(self, key, item):
        """
        Puts a key/value pair into cache.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets the value associated with given key from the cache.
        """
        return self.cache_data.get(key, None)
