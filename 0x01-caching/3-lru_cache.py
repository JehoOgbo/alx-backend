#!/usr/bin/env python3
''' LRUCache module
'''
BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    ''' caching system that discards the least recently used item
    '''
    def __init__(self):
        ''' initialize the class
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' puts item into the cache following least recently used algorithm
        '''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        ''' gets the item linked to key
        '''
        if key is None:
            return None
        try:
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data[key]
        except:
            return None
