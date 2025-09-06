# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sentinel = cur = ListNode()
        while l1 or l2:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = s // 10
            s %= 10
            cur.next = ListNode(val=s)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        cur.next = ListNode(val=carry) if carry else None
        return sentinel.next

# leetcode submit region end(Prohibit modification and deletion)
