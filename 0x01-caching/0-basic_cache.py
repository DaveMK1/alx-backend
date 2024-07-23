#!/usr/bin/env python3
"""BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Provides functionality for storing and retrieving
    items in a dictionary
    """
    def put(self, key, item):
        """Inserts an item into the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Fetches an item using its key
        """
        return self.cache_data.get(key, None)
