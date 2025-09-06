# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0 or n & (n - 1) != 0:
            return False
        one = n & (-n)
        x, count = 1, 0
        while x != one:
            x <<= 1
            count += 1
        return (count & 1) == 0

# leetcode submit region end(Prohibit modification and deletion)
