#!/usr/bin/env python3
"""script to insert documents based on
**kwargs to collection
"""

def insert_school(mongo_collection, **kwargs):
    """inserts a new document to a collection"""
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id if data else None
