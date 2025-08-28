# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # merge sort
        if not head or not head.next:
            return head
        mid = self.middle_node(head)
        head1 = self.sortList(head)
        head2 = self.sortList(mid)
        return self.partition(head1, head2)

    def middle_node(self, node: ListNode) -> ListNode:
        pre = slow = fast = node
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        return slow

    def partition(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = cur = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return sentinel.next

# leetcode submit region end(Prohibit modification and deletion)
