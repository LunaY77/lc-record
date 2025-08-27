# leetcode submit region begin(Prohibit modification and deletion)
b = {'(':')', '{':'}', '[':']'}
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in b:
                st.append(c)
            else:
                if not st or c != b[st.pop()]:
                    return False
        return not st

# leetcode submit region end(Prohibit modification and deletion)
