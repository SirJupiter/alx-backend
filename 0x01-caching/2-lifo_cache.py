#!/usr/bin/env python3
"""LIFO caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching"""
    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Assigns the item valur for the key"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.stack.pop()
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets the value in self.cache_data"""
        return self.cache_data.get(key)
