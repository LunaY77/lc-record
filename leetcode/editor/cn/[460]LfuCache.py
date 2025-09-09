# leetcode submit region begin(Prohibit modification and deletion)
class ListNode:
    __slots__ = 'prev', 'next', 'key', 'value', 'freq'

    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.freq = 1

class LFUCache:

    def __init__(self, capacity: int):
        self.key_to_node = dict()
        self.capacity = capacity
        def new_list():
            sentinel = ListNode()
            sentinel.prev = sentinel
            sentinel.next = sentinel
            return sentinel
        self.freq_to_sentinel = defaultdict(new_list)

    def get_node(self, key):
        if key not in self.key_to_node:
            return None
        node = self.key_to_node[key]
        self.remove(node)
        sentinel = self.freq_to_sentinel[node.freq]
        if sentinel.prev is sentinel:
            del self.freq_to_sentinel[node.freq]
            if node.freq == self.min_freq:
                self.min_freq += 1
        node.freq += 1
        sentinel = self.freq_to_sentinel[node.freq]
        self.push_front(sentinel, node)
        return node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def push_front(self, sentinel, node):
        node.next = sentinel.next
        node.prev = sentinel
        sentinel.next.prev = node
        sentinel.next = node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.value = value
            return
        if len(self.key_to_node) == self.capacity:
            sentinel = self.freq_to_sentinel[self.min_freq]
            tail = sentinel.prev
            self.remove(tail)
            del self.key_to_node[tail.key]
            if sentinel.prev is sentinel:
                del self.freq_to_sentinel[self.min_freq]
        self.key_to_node[key] = node = ListNode(key, value)
        sentinel = self.freq_to_sentinel[1]
        self.push_front(sentinel, node)
        self.min_freq = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value))
# leetcode submit region end(Prohibit modification and deletion)
