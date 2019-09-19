from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """

    def __init__(self, limit=10):
        self.list = DoublyLinkedList()
        self.storage = {}
        self.limit = limit

    """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """

    def get(self, key):
        if key in self.storage:
            found = self.storage[key]

            self.list.delete(found)
            self.list.add_to_head(found)
            return found.value
        else:
            return None

    """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """

    def set(self, key, value):
      if key in self.storage:
        found = self.storage[key]
        found.value = value

        if self.list.head is not found:
          self.list.delete(found)
          self.list.add_to_head(found)
        else:
          new_node = DoublyLinkedList(value)
          if self.list.get_max() == self.limit:
            self.storage.pop(key)
            self.list.delete(found)
          self.list.add_to_head(new_node)
          self.storage[key] = new_node
