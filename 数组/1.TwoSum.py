#
# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
#
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i,n in enumerate(nums):
            if target-n in nums_dict:
                return [nums_dict[target-n],i]
            nums_dict[n]=i
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []

        d = dict()

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            n = target - nums[i]
            if n in d and i is not d[n]:
                return [d[n],i]

        return []