#!/usr/bin/python3
""" LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.count_dict = {}
        self.frequency_dict = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data and BaseCaching.MAX_ITEMS > 0:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                lowest_count = dict(sorted(self.frequency_dict.items()))
                lowest_count = list(lowest_count.keys())[0]
                print(lowest_count)
                key_to_delete = self.frequency_dict.get(lowest_count)[0]
                self.frequency_dict.get(lowest_count).pop()
                if len(self.frequency_dict.get(lowest_count)) == 0:
                    del self.frequency_dict[lowest_count]
                del self.cache_data[key_to_delete]
                del self.count_dict[key_to_delete]
                print("DISCARD:", key_to_delete)
            self.cache_data[key] = item
            self.count_dict[key] = 1
            f_key = 1
            if f_key not in self.frequency_dict:
                self.frequency_dict[f_key] = []
                self.frequency_dict[f_key].append(key)
        elif BaseCaching.MAX_ITEMS > 0:
            self.cache_data[key] = item
            frequency = self.count_dict.get(key)
            self.frequency_dict.get(frequency).remove(key)
            if len(self.frequency_dict.get(frequency)) == 0:
                del self.frequency_dict[frequency]
            f_key = frequency + 1
            if f_key not in self.frequency_dict:
                self.frequency_dict[f_key] = []
                self.frequency_dict[f_key].append(key)
            self.count_dict[key] = 1 + frequency

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        frequency = self.count_dict.get(key)
        if key in self.frequency_dict.get(frequency):
            self.frequency_dict.get(frequency).remove(key)
        if len(self.frequency_dict.get(frequency)) == 0:
            del self.frequency_dict[frequency]
        if frequency not in self.frequency_dict:
            self.frequency_dict[frequency + 1] = [key]
        self.count_dict[key] = frequency + 1
        return self.cache_data.get(key)
