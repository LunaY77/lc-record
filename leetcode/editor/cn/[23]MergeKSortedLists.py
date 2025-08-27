# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
ListNode.__lt__ = lambda a, b: a.val < b.val
class Solution:
     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
         sentinel = cur = ListNode()
         heap = [head for head in lists if head]
         heapify(heap)
         while heap:
             node = heappop(heap)
             cur.next = node
             if node.next:
                 heappush(heap, node.next)
             cur = cur.next
         return sentinel.next

# leetcode submit region end(Prohibit modification and deletion)
