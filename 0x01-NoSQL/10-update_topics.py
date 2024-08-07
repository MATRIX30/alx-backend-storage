#!/usr/bin/env python3
""" module to update data in mongodb"""


def update_topics(mongo_collection, name, topics):
    """method to update topic

    Args:
        mongo_collection (collection): mongodb collection
        name (str): the name of the school to update
        topics (list): list of topics to update
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
