#!/usr/bin/env python3
"""BaseCaching module
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Defines an object that facilitates storing and
    fetching items from a dictionary with a FIFO
    eviction policy once the limit is surpassed
    """
    def __init__(self):
        """Initializes the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Inserts an item into the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Fetches an item using its key
        """
        return self.cache_data.get(key, None)
