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
        """constructor"""
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        method takes data argument and returns string
        """
        redis_key = str(uuid.uuid4())
        self.__redis.set(redis_key, data)
        return redis_key
