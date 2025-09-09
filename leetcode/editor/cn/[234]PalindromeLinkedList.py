# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.middle_node(head)
        tail = self.reverse(mid)
        while head and head.next:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True

    def middle_node(self, node):
        slow = fast = node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, node):
        pre, cur = None, node
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

# leetcode submit region end(Prohibit modification and deletion)
