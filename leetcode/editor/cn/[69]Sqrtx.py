# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = -1, 2**31 - 1
        while l + 1 < r:
            mid = (l + r) >> 1
            if mid * mid <= x:
                l = mid
            else:
                r = mid
        return l

# leetcode submit region end(Prohibit modification and deletion)
