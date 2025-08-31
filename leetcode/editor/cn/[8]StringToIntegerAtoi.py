# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        flag = True
        i = 0
        if s[0] == '-':
            flag = False
            i = 1
        elif s[0] == '+':
            i = 1
        res = 0
        while i < len(s) and '0' <= s[i] <= '9':
            res = res * 10 + int(s[i])
            if flag and res >= 2**31 - 1:
                return 2**31 - 1
            elif not flag and res >= 2**31:
                return -2**31
            i += 1
        return res if flag else -res
        
# leetcode submit region end(Prohibit modification and deletion)
