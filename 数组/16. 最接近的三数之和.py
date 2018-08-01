#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
l = [1,2,3]
del l[1]
print(l)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #nums = sorted(nums)
        close = 2**31-1
        close_index = 2**31-1
        for i in range(0,len(nums)):
            if abs(nums[i]-target)<close:
                close = abs(nums[i]-target)
                close_index = i
        temp = nums[close_index]
        del nums[close_index]
        nums = sorted(nums)
        left = 0
        right = len(nums)-1
        close_2 = 2**31-1
        min1 = 0

        while left!=right:
            if abs(target-(nums[left]+nums[right]+temp))<close_2:
                close_2 = abs(target-(nums[left]+nums[right]+temp))
                min1 = nums[left]+nums[right]
            if    target-(nums[left]+nums[right]+temp)<0:
                right = right-1
            elif target-(nums[left]+nums[right]+temp)==0:
                return min1+temp
            else:
                left = left+1

        return min1+temp
a = Solution()
print(a.threeSumClosest([1,2,5,10,11],12))


