#!usr/bin/env python3
"""redis basics """
import redis
import uuid

class Cache():
    """ dfjskf"""
    def __init__():
        """dfjh"""
        _redis=r.Redis()
        r.flushdb()
    def store(data):
        """dsfjh"""
        id=uuid.uuid1()
        _redis.set(id, data)
        return id
