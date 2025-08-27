# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.middle_node(head)
        tail = self.reverse(mid)
        while tail and tail.next:
            nxt1 = head.next
            nxt2 = tail.next
            head.next = tail
            tail.next = nxt1
            head = nxt1
            tail = nxt2

    def reverse(self, node: ListNode) -> ListNode:
        pre, cur = None, node
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def middle_node(self, node: ListNode) -> ListNode:
        slow = fast = node
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# leetcode submit region end(Prohibit modification and deletion)
