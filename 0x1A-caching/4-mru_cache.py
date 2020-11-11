#!/usr/bin/python3

"""
4. MRU Caching
"""

from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class. Inherits from BaseCaching.
    """

    def __init__(self):
        """
        Constructor.
        """
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """
        Puts a key/value pair into cache.
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif self.is_full():
                self.evict()
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets the value associated with given key from the cache.
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key)

    def is_full(self):
        """
        Determines if cache is full.
        """
        return len(self.cache_data) >= self.MAX_ITEMS

    def evict(self):
        """
        Evicts last key out of cache/queue.
        """
        popped = self.queue.pop()
        del self.cache_data[popped]
        print("DISCARD: " + str(popped))
