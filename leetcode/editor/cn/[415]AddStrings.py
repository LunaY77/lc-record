# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        n, m = len(num1), len(num2)
        i, j = n - 1, m - 1
        ans = ''
        while i >= 0 or j >= 0:
            s = (int(num1[i]) if i >= 0 else 0) + (int(num2[j]) if j >= 0 else 0) + carry
            carry = s // 10
            ans = str(s % 10) + ans
            i -= 1
            j -= 1
        return str(carry) + ans if carry else ans


# leetcode submit region end(Prohibit modification and deletion)
