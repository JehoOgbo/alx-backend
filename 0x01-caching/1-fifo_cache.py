#!/usr/bin/env python3
''' class FIFOCache
'''
BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    ''' FIFOCache
      - uses first in first out to manage cache
      - contains put method to input new items
      - contains get method to get items from the cache
      - can handle a fixed number of items defined by BaseCaching.MAX_ITEMS
    '''
    def __init__(self):
        ''' Make the cache ordered
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' Assign a new item to the cache
            if the number of items in the cache is higher that the max,
              - discard the first item in the cache
              - print discard with the discarded key
            to make room
        '''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", first_key)

    def get(self, key):
        ''' get a value from the cache
        '''
        if key is None:
            return None
        try:
            return self.cache_data[key]
        except KeyError:
            return None
