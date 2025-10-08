# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = set()
        n = len(s)
        l = r = 0
        ans = 0
        while r < n:
            while s[r] in x:
                x.remove(s[l])
                l += 1
            x.add(s[r])
            r += 1
            ans = max(ans, r - l)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
