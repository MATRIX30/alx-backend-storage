#!/usr/bin/env python3
""" script to list all dababased in mongodb"""
def list_all(mongo_collection):
    """method to list all documents in a mongo collection"""
    docs = mongo_collection.find()
    return docs if docs else []
