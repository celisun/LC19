# what are we caching?  caching the results of web queries
# do we assume all inputs are valid or do we validate them
# do we assume this fits memory? yes


class Node:
    def __init__(self, k, v):
        self.query = k
        self.results = v
        self.next = None
        self.prev = None


class DoublyLinkedLlist:
    def __init__(self):
        self.size = 0
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    # def print(self):
    #     res = []
    #     head = self.head.next
    #     for __ in range(self.size):
    #         res.append([head.query, head.results])
    #         head = head.next
    #     print (res)
    #     return

    def _add_(self, node):  # add to back reset tail
        self.tail.prev.next, node.prev = node, self.tail.prev
        node.next, self.tail.prev = self.tail, node
        self.size += 1

    def _remove_(self, node):  # update to the back
        # remove node
        if not node: return
        node.prev.next, node.next.prev = node.next, node.prev
        self.size -= 1

    def pop_front(self):  # retrieve lru
        if not self.size: return
        self._remove_(self.head.next)

    def update(self, node):
        self._remove_(node)
        self._add_(node)

    def add(self, node):
        self._add_(node)

class Cache:
    def __init__(self, MAX_SIZE):
        self.MAX_SIZE = MAX_SIZE
        self.size = 0
        self.data = {}
        self.linked_list = DoublyLinkedLlist()

    def get(self, query):
        """if not such query in cache (cahce miss), return None.
        Otherwise, update it frequency and return its results from data"""

        node = self.data.get(query)
        if not node: return None
        self.linked_list.update(node)
        return node.results

    def set(self, results, query):
        """If exisiting key, replace the value and update its frequency (remove
        and add to back).
        If new key, invalidate LRU entry if necessary (cache size full), then
        add to data and add to the frequency list"""

        node = self.data.get(query)
        if node is not None:
            node.results = results
            self.linked_list.update(node)
        else:
            if self.size == self.MAX_SIZE:
                self.data.pop(self.linked_list.head.next.query)
                self.linked_list.pop_front()
            else:
                self.size += 1
            node = Node(query, results)
            self.linked_list.add(node)
            self.data[query] = node


cache = Cache(2)
cache.set(1,1)
cache.set(2,2)
print(cache.get(2))
cache.set(5,5)
# cache.linked_list.print()

