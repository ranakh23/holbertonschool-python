#!usr/bin/env python3
"""redis basics """
import redis
import uuid


class Cache():
    """ dfjskf"""
    def __init__(self):
        """dfjh"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """dsfjh"""
        id = uuid.uuid1()
        self._redis.set(id, data)
        return id
