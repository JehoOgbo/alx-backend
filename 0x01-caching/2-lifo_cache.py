#!/usr/bin/env python3
''' LIFOCache
'''
BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    ''' LIFOCache
        Implements a last in first out cache system
    '''
    def __init__(self):
        ''' Enforce ordering in the cache
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' add new item to the cache using lifo
        '''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                key, _ = self.cache_data.popitem(last=True)
                print('DISCARD:', key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        ''' get an item from the cache
        '''
        if key is None:
            return None
        try:
            return self.cache_data[key]
        except KeyError:
            return None
