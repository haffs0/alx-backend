#!/usr/bin/python3
""" LRUCache module
"""
from base_caching import BaseCaching


class Node:
    """ Node defines
    """
    def __init__(self, k, v):
        """ Initiliaze
        """
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache(BaseCaching):
    """ LRUCache defines:
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

        """head and tail of the linkedlist"""
        self.head = Node("#", 0)
        self.tail = Node("_", 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self._remove(self.cache_data.get(key))
        newNode = Node(key, item)
        self._add(newNode)
        self.cache_data[key] = newNode
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            nodeToRemove = self.tail.prev
            self._remove(nodeToRemove)
            print("DISCARD:", nodeToRemove.key)
            del self.cache_data[nodeToRemove.key]

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        node = self.cache_data.get(key)
        self._remove(node)
        self._add(node)
        return node.val

    def _remove(self, node):
        """remove node"""
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = node.next
        nextNode.prev = prevNode

    def _add(self, node):
        """add node"""
        nextNode = self.head.next
        prevNode = self.head
        prevNode.next = node
        nextNode.prev = node
        node.next = nextNode
        node.prev = prevNode

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key).val))
