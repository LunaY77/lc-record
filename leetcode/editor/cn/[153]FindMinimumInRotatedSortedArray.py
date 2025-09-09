# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = -1, n
        while l + 1 < r:
            mid = (l + r) >> 1
            if nums[mid] > nums[-1]:
                l = mid
            else:
                r = mid
        return nums[r]
        
# leetcode submit region end(Prohibit modification and deletion)
