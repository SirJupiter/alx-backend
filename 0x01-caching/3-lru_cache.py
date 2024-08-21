#!/usr/bin/env python3
"""LRU caching"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching"""
    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Assigns the item valur for the key"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.queue.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets the value in self.cache_data"""
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data.get(key)
