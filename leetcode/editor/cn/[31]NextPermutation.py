# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if not nums:
            return
        n = len(nums)
        i = n - 2
        # 找到第一个小于右侧数字的 index
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i != -1:
            j = n - 1
            # 找到 i 右侧第一个大于 nums[i] 的 index
            while j > i and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # 倒序排列 i 右侧数字
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

# leetcode submit region end(Prohibit modification and deletion)
