# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        path = [0] * 4
        def dfs(i, j):
            if j == 4:
                if i == n:
                    ans.append('.'.join([str(x) for x in path]))
                return
            if i == n:
                return
            if s[i] == '0':
                path[j] = 0
                dfs(i + 1, j + 1)
                return
            res = 0
            for k in range(i, n):
                res = res * 10 + int(s[k])
                if 0 <= res <= 0xff:
                    path[j] = res
                    dfs(k + 1, j + 1)
                else:
                    return
        dfs(0, 0)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
