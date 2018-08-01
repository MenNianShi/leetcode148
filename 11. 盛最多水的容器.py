#
# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。画 n 条垂直线，使得垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 注意：你不能倾斜容器，n 至少是2。

# 主要的困惑在于如何移动双指针才能保证最大的盛水量被遍历到
# 假设有左指针left和右指针right，且left指向的值小于right的值，假如我们将右指针左移，则右指针左移后的值和左指针指向的值相比有三种情况
#
# 右指针指向的值大于左指针
# 这种情况下，容器的高取决于左指针，但是底变短了，所以容器盛水量一定变小
#
# 右指针指向的值等于左指针
# 这种情况下，容器的高取决于左指针，但是底变短了，所以容器盛水量一定变小
#
# 右指针指向的值小于左指针
# 这种情况下，容器的高取决于右指针，但是右指针小于左指针，且底也变短了，所以容量盛水量一定变小了
#
# 综上所述，容器高度较大的一侧的移动只会造成容器盛水量减小
# 所以应当移动高度较小一侧的指针，并继续遍历，直至两指针相遇。
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        start =0
        end = len(height)-1
        while start!=end:
            minheight = min(height[start],height[end])
            curArea = minheight*(end-start)
            res = max(curArea,res)
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        return res