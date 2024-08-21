#!/usr/bin/env python3
"""LFU caching"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """LFU caching"""
    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns the item valur for the key"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = min(self.cache_data, key=self.cache_data.get)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

            self.cache_data[key] = item

    def get(self, key):
        """Gets the value in self.cache_data"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
