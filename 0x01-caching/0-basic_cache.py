#!/usr/bin/env python3
""" BasicCache
    caching system that inherits from BaseCaching
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCaching defines:
      - a limitless caching system
      - put and get methods for this system
    """
    def put(self, key, item):
        """ Assign to self.cache_data the item value for key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value in the cache linked to the key
        """
        if key is None:
            return None
        try:
            return self.cache_data[key]
        except KeyError:
            return None
