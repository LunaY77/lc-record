# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append((root, 0))
        ans = defaultdict(lambda: -101)
        while q:
            node, layer = q.popleft()
            if ans[layer] == -101:
                ans[layer] = node.val
            if node.right:
                q.append((node.right, layer + 1))
            if node.left:
                q.append((node.left, layer + 1))
        return list(ans.values())
        
# leetcode submit region end(Prohibit modification and deletion)
