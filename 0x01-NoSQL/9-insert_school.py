#!/usr/bin/env python3
"""
Insert a new document in a collection using kwargs
Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be pymongo collection object
Returns new _id
"""


def insert_school(mongo_collection, **kwargs):
    """
    Prototype: def insert_school(mongo_collection, **kwargs):
    Returns the new _id
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
