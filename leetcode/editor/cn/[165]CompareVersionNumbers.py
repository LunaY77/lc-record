# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = [int(x) for x in version1.split('.')]
        arr2 = [int(x) for x in version2.split('.')]
        i = j = 0
        n, m = len(arr1), len(arr2)
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                return -1
            elif arr1[i] > arr2[j]:
                return 1
            i += 1
            j += 1
        while i < n:
            if arr1[i] > 0:
                return 1
            i += 1
        while j < m:
            if arr2[j] > 0:
                return -1
            j += 1
        return 0

# leetcode submit region end(Prohibit modification and deletion)
