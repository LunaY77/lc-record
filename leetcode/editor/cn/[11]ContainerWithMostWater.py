# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        l, r = 0, n - 1
        while l < r:
            cur = min(height[l], height[r]) * (r - l)
            ans = max(ans, cur)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
