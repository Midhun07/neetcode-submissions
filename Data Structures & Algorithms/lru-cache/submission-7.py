# dict for get. store key, (value, pointer). For every get delete the pointer from list and update the list and dict with new node for the value. For put maintain a global len which if > capacity the remove from left of list and dict and add the node to the right. For this the LL should be double LL.
class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.start, self.end = Node(-1,-1), Node(-1,-1)
        self.start.next, self.end.prev = self.end, self.start

    def delete(self, key):
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.cache[key]
        return node
    
    def add(self, node):
        self.end.prev.next = node
        node.next = self.end
        node.prev = self.end.prev
        self.end.prev = node
        self.cache[node.key] = node
    
    def update(self, key, value=None):
        node = self.delete(key)
        node.val = value if value is not None else node.val
        self.add(node)

    def get(self, key: int) -> int:
        item = self.cache.get(key)
        if item:
            self.update(key)
            return item.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key):
            self.update(key, value)
        else:
            if len(self.cache) == self.cap:
                self.delete(self.start.next.key)
            self.add(Node(key, value))
