#
# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:
#
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
class Interval(object):
    def __init__(self,s =0,e = 0):
        self.start = s
        self.end = e
class Solution(object):
    def merge(self,intervals):

        intervals.sort(key= lambda x:x.start)
        merged = []
        for interval in intervals:
            if not merged or interval.start>merged[-1].end:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end,interval.end)
        return merged
