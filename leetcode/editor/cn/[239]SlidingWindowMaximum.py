# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        r = 0
        ans = []
        for r in range(n):
            while q and q[0] <= r - k:
                q.popleft()
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if r >= k - 1:
                ans.append(nums[q[0]])
        return ans

# leetcode submit region end(Prohibit modification and deletion)
