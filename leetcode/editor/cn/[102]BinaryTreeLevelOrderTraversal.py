# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = defaultdict(list)
        q = deque()
        q.append((root, 0))
        while q:
            node, layer = q.popleft()
            ans[layer].append(node.val)
            if node.left:
                q.append((node.left, layer + 1))
            if node.right:
                q.append((node.right, layer + 1))
        return list(ans.values())

# leetcode submit region end(Prohibit modification and deletion)
