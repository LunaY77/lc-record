# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        n = len(nums)
        l, r = -1, n
        while l + 1 < r:
            mid = (l + r) >> 1
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        ans[0] = r if r < n and nums[r] == target else -1
        l, r = -1, n
        while l + 1 < r:
            mid = (l + r) >> 1
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        ans[1] = l if l >= 0 and nums[l] == target else -1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
