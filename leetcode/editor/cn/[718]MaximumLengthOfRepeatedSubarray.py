# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        ans = 0
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                if x == y:
                    tmp = dp[i + 1][j + 1] = dp[i][j] + 1
                    ans = max(ans, tmp)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
