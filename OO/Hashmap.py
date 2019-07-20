class Item:
    def __init__(self, k, v):
        self.k = k
        self.v = v
# use chaining for has collision, within each bucket, use linear time analysis for lookup


# clarification
# are keys integers only ?
# use chaining for collision resolution ? yes
# do we worry about load factor? no
# do we assume all inputs are valid or do we need to validate them ?
# do we assume this fits memory  yes

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.data = [[] for __ in xrange(self.size)]

    def _hash_function(self, key):
        return key % self.size

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_index = self._hash_function(key)
        for item in self.data[hash_index]:
            if item.k == key:
                item.v = value
                return
        self.data[hash_index].append(Item(key, value))
        return

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hash_index = self._hash_function(key)
        for item in self.data[hash_index]:
            if item.k == key:
                return item.v

        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hash_index = self._hash_function(key)
        for i, item in enumerate(self.data[hash_index]):
            if item.k == key:
                del self.data[hash_index][i]
                return
                # raise KeyError('key not found')

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)