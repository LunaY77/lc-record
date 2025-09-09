# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i, n = 0, len(nums)
        while i < n:
            ti = nums[i] - 1
            if nums[ti] != nums[i]:
                nums[ti], nums[i] = nums[i], nums[ti]
            else:
                i += 1
        return [x for i, x in enumerate(nums) if i != x - 1]

# leetcode submit region end(Prohibit modification and deletion)
