#!/usr/bin/env python3
"""
Module contains Cache class
"""


import redis
import uuid
from typing import Union


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
        """
        redis_key = str(uuid.uuid4())
        self._redis.set(redis_key, data)
        return redis_key
