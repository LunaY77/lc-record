# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

        # dfs
#         n = len(nums)
#         @cache
#         def dfs(i):
#             res = 1
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     res = max(res, dfs(j) + 1)
#             return res
#         return max([dfs(i) for i in range(n)])

# leetcode submit region end(Prohibit modification and deletion)
