# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # merge_sort
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

    def merge_sort(self, nums):
        if not nums or len(nums) == 1:
            return nums
        mid = len(nums) // 2
        arr1 = self.merge_sort(nums[:mid])
        arr2 = self.merge_sort(nums[mid:])
        return self.merge(arr1, arr2)

    def merge(self, arr1, arr2):
        res = []
        n, m = len(arr1), len(arr2)
        i = j = 0
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        while i < n:
            res.append(arr1[i])
            i += 1
        while j < m:
            res.append(arr2[j])
            j += 1
        return res

    # quick_sort
#     def sortArray(self, nums: List[int]) -> List[int]:
#         self.quick_sort(nums, 0, len(nums) - 1)
#         return nums
#
#     def quick_sort(self, nums, l, r):
#         if l >= r:
#             return
#         le, gt = self.partition(nums, l, r)
#         self.quick_sort(nums, l, le - 1)
#         self.quick_sort(nums, gt, r)
#
#     def partition(self, nums, l, r):
#         pi = random.randint(l, r)
#         nums[l], nums[pi] = nums[pi], nums[l]
#         pivot = nums[l]
#
#         le, gt = l, r + 1
#         i = l + 1
#
#         while i < gt:
#             if nums[i] < pivot:
#                 nums[i], nums[le] = nums[le], nums[i]
#                 i += 1
#                 le += 1
#             elif nums[i] > pivot:
#                 gt -= 1
#                 nums[gt], nums[i] = nums[i], nums[gt]
#             else:
#                 i += 1
#         return le, gt

# leetcode submit region end(Prohibit modification and deletion)
