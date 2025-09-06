# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([x.strip() for x in s.split(' ') if x][::-1])
        
# leetcode submit region end(Prohibit modification and deletion)
