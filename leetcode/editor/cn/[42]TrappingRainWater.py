# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [0] * n
        suf_max = [0] * n
        pre_max[0] = height[0]
        suf_max[-1] = height[-1]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])
        ans = 0
        for i in range(n):
            ans += max(0, min(pre_max[i], suf_max[i]) - height[i])
        return ans

# leetcode submit region end(Prohibit modification and deletion)
