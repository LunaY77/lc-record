# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(0, dp[i - 1]) + nums[i]
        return max(dp)

# leetcode submit region end(Prohibit modification and deletion)
