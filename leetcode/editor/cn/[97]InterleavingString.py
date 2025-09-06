# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False
        @cache
        def dfs(i, j, k):
            if i < 0 and j < 0:
                return True
            res = False
            if i >= 0 and s1[i] == s3[k]:
                res = res or dfs(i - 1, j, k - 1)
            if j >= 0 and s2[j] == s3[k]:
                res = res or dfs(i, j - 1, k - 1)
            return res
        return dfs(n - 1, m - 1, len(s3) - 1)

# leetcode submit region end(Prohibit modification and deletion)
