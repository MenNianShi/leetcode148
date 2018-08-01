#
# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
# 示例 1:
#
# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
# 示例 2:
#
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
class Interval(object):
    def __init__(self,s =0,e = 0):
        self.start = s
        self.end = e
class Solution(object):
    def insert(self,intervals,newInterval):
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x.start)
        merged = []
        for interval in intervals:
            if not merged or interval.start>merged[-1].end:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end,interval.end)
        return merged
