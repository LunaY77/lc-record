# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        intervals = sorted(intervals)
        l, r = intervals[0][0], intervals[0][1]
        for i in range(1, n):
            cur_l, cur_r = intervals[i][0], intervals[i][1]
            if r >= cur_l:
                r = max(r, cur_r)
            else:
                ans.append([l, r])
                l, r = cur_l, cur_r
        ans.append([l, r])
        return ans


# leetcode submit region end(Prohibit modification and deletion)
