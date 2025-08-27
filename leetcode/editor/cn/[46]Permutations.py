# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = [-1] * n
        ans = []
        vis = [False] * n
        def dfs(step):
            if step == n:
                ans.append(path.copy())
                return
            for j in range(n):
                if not vis[j]:
                    vis[j] = True
                    path[step] = nums[j]
                    dfs(step + 1)
                    vis[j] = False
        dfs(0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
