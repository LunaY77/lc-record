# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = -1, len(nums)
        while l + 1 < r:
            mid = (l + r) >> 1
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        return l if nums[l] == target else -1
        
# leetcode submit region end(Prohibit modification and deletion)
