# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = p0 = ListNode(next=head)
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        while fast:
            p0 = slow
            slow = slow.next
            fast = fast.next
        p0.next = slow.next
        return sentinel.next

# leetcode submit region end(Prohibit modification and deletion)
