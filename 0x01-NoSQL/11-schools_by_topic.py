#!/usr/bin/env python3
"""module to return schools with specific topics"""


def schools_by_topic(mongo_collection, topic):
    """get schools by a specific topic"""
    return [mongo_collection.find({"topic": })]