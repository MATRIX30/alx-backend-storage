#!/usr/bin/env python3
"""
Module contains Cache class
"""


import redis
import uuid
from typing import Union, Callable, Any


class Cache:
    """
    class to store cache information about client
    """

    def __init__(self) -> None:
        """
        creates a new redis cache object
        that would be used to read and write to redis store
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        method takes data argument and stores in redis store and
        returns string key to that data
        """
        redis_key = str(uuid.uuid4())
        self._redis.set(redis_key, data)
        return redis_key
    
    def get(self, key:str, fn:Callable = None) -> Any:
        """
        Method to get data stored in a given key
        """
        if (self._redis.get(key) == None):
            return None
        data = self._redis(key)
        return fn(data)
    
    def get_str(self, key: str) -> str:
        """
        method to process getting strings from redis
        """
        self.get(key, lambda x: self._redis)