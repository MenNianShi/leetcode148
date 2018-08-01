# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
#
# 示例:
#
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
# 进阶：
#
# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？
# 分析：
#
# 输出的结果形式为[0]*[1]*[2]*
# 统计0和2的个数rNums和bNums，并在遍历过程中，将已遍历元素修改为1
# 遍历结束后，将前rNums个元素改为0，末尾bNums个元素改为2

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            rNums = 0
            bNums = 0
            for i,x in enumerate(nums):
                if x == 0: rNums += 1
                if x == 2: bNums += 1
                nums[i] = 1
            if rNums:
                nums[:rNums] = [0] * rNums
            if bNums:
                nums[-bNums:] = [2] * bNums
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        colors_count = [0 for i in range(3)]
        for num in nums:
            colors_count[num] += 1
        j = 0
        for i in range(length):
            while colors_count[j] == 0:
                j += 1
            nums[i] = j
            i += 1
            colors_count[j] -= 1