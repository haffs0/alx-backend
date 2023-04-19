#!/usr/bin/python3
""" LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.dp = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.dp) == BaseCaching.MAX_ITEMS:
                # delete least recently used element
                last = self.dp[-1]
                # Pops the last element
                ele = self.dp.pop()
                print("DISCARD:", last)
                # Erase the last
                del self.cache_data[last]
        else:
            del self.dp[0]

        # update reference
        if key in self.dp:
            self.dp.remove(key)
            self.dp.insert(0, key)
            del self.cache_data[key]
            self.cache_data[key] = item
        else:
            self.dp.insert(0, key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        item = self.cache_data.get(key, None)
        if key in self.dp:
            self.dp.remove(key)
            self.dp.insert(0, key)
        return item
