# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return -1
            l = dfs(node.left) + 1
            r = dfs(node.right) + 1
            ans = max(ans, l + r)
            return max(l, r)
        dfs(root)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
