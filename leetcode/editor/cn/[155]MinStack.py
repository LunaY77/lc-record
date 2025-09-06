# leetcode submit region begin(Prohibit modification and deletion)
class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        _, cur_min = self.st[-1] if self.st else (0, inf)
        self.st.append((val, min(val, cur_min)))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        x, _ = self.st[-1]
        return x

    def getMin(self) -> int:
        _, x = self.st[-1]
        return x


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)
