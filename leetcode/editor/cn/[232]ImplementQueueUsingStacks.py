# leetcode submit region begin(Prohibit modification and deletion)
class MyQueue:

    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        if not self.b:
            self.transfer()
        return self.b.pop()

    def transfer(self):
        while self.a:
            self.b.append(self.a.pop())

    def peek(self) -> int:
        if not self.b:
            self.transfer()
        return self.b[-1]

    def empty(self) -> bool:
        return not (self.a or self.b)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# leetcode submit region end(Prohibit modification and deletion)
