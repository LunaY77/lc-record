# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            ti = nums[i] - 1
            if 0 <= ti < n and nums[ti] != nums[i]:
                nums[ti], nums[i] = nums[i], nums[ti]
                continue
            i += 1
        for i, x in enumerate(nums):
            if x - 1 != i:
                return i + 1
        return n + 1


# leetcode submit region end(Prohibit modification and deletion)
