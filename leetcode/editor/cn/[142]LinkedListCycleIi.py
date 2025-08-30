# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # proof:
        # 假设 head 到环起始点的距离为 a，环长为 b
        # 第一次相遇时，slow 走了距离 c，那么 fast 走了 2c, 设 fast 在环中走了 k 圈
        # 有 2c - c = kb
        # c = kb
        # 也就是说 slow 在环中走了 c - a = kb - a
        # 那么 slow 在走 a 步就可以回到入环口
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                slow = head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
        
# leetcode submit region end(Prohibit modification and deletion)
