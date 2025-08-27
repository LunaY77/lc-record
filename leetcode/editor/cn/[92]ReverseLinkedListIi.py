# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        n = right - left + 1
        sentinel = p0 = ListNode(next=head)
        for _ in range(left - 1):
            p0 = p0.next
        pre, cur = None, p0.next
        for _ in range(n):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        p0.next.next = cur
        p0.next = pre
        return sentinel.next

# leetcode submit region end(Prohibit modification and deletion)
