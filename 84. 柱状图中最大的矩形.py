# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
class Solution(object):
    def largestRectangleArea(self, heights):#单调栈？
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[-1]
        ans=0
        size=len(heights)
        heights.append(0)
        for i in range(size+1):
            while heights[i]<heights[stack[-1]]:
                h=heights[stack.pop()]
                w=i-stack[-1]-1
                area=h*w
                if area>ans:
                    ans=area
            stack.append(i)
        return ans