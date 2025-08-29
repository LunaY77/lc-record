# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = pre = ListNode(next=head)
        cur = head
        while cur:
            flag = False
            while cur.next and cur.val == cur.next.val:
                flag = True
                cur = cur.next
            cur = cur.next
            if flag:
                pre.next = cur
            else:
                pre = pre.next
        return sentinel.next

# leetcode submit region end(Prohibit modification and deletion)
