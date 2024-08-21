#!/usr/bin/env python3
"""Basic dictionary"""

import base_caching


class BasicCache(base_caching.BaseCaching):
    """Defines a dictionary"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()

    def put(self, key, item):
        """Assigns the item valur for the key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Gets the value in self.cache_data"""
        if key and key in self.cache_data:
            return self.cache_data.get(key)

        return None
