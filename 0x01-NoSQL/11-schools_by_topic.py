#!/usr/bin/env python3
"""
Prototype: def schools_by_topic(mongo_collection, topic):
mongo_collection will be a pymongo collection object
Returns list of schools with a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Prototype: def schools_by_topic(mongo_collection, topic):
    Return list of schools having a specific topic
    """
    return mongo_collection.find({"topics": topic})
