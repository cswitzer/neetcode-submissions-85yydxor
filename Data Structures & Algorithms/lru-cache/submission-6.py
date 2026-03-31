class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.cache = {}

    def insert_head(self, node):
        if not self.head:
            self.head = self.tail = node
            return

        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            # remove curr head
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            # remove curr tail
            self.tail = node.prev

        node.prev = node.next = None

    def pop_tail(self):
        if not self.tail:
            return None

        node = self.tail
        self.remove(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
        else:
            node = Node(key, value)
            self.cache[key] = node

        self.insert_head(node)

        if len(self.cache) > self.capacity:
            lru = self.pop_tail()
            del self.cache[lru.key]
