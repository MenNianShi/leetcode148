# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
#
# 示例 1:
#
# 输入: [1,2,0]
# 输出: 3
# 示例 2:
#
# 输入: [3,4,-1,1]
# 输出: 2
# 示例 3:
#
# 输入: [7,8,9,11,12]
# 输出: 1
# 交换数组元素，使得数组中第i位存放数值(i+1)。最后遍历数组，寻找第一个不符合此要求的元素，返回其下标。整个过程需要遍历两次数组，复杂度为O(n)。


class Solution(object):
    def firstMissingPositive(self, nums):
        i, n = 0, len(nums)
        while i < n:
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # swap
                temp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[temp - 1] = temp
            else:
                i += 1
        for i, v in enumerate(nums):
            if v != i + 1:
                return  i + 1
        return n + 1
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i in nums:
            i+=1
        return i
