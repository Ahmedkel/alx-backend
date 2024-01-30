#!/usr/bin/env python3
""" MRU Caching """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU Caching """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.mru_keys = []

    def put(self, key, item):
        """ Put Method """
        if key and item:
            if key in self.cache_data:
                self.mru_keys.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                print("DISCARD: {}".format(self.mru_keys[-1]))
                del self.cache_data[self.mru_keys[-1]]
                self.mru_keys.pop()
            self.mru_keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get Method """
        if key in self.cache_data:
            self.mru_keys.remove(key)
            self.mru_keys.append(key)
            return self.cache_data[key]
        return None
