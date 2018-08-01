
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic = {}
        for ele in nums:
            if ele not in dic:
                dic[ele] = 0
            dic[ele] += 1

        if 0 in dic and dic[0] > 2:
            rst = [[0, 0, 0]]
        else:
            rst = []

        pos = [p for p in dic if p > 0]
        neg = [n for n in dic if n < 0]

        for p in pos:
            for n in neg:
                inverse = -(p + n)
                if inverse in dic:
                    if inverse == p and dic[p] > 1:
                        rst.append([n, p, p])
                    elif inverse == n and dic[n] > 1:
                        rst.append([n, n, p])
                    elif inverse < n or inverse > p or inverse == 0:
                        rst.append([n, inverse, p])

        return rst
class Solution:#超时
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        for target in nums:
            start = 0
            end = len(nums)-1
            while start!=end:
                if nums[start]+nums[end] == -target:
                    res.append([nums[start],nums[end],target])
                elif nums[start]+nums[end] > -target:
                    end = end-1
                else:
                    start=start+1
        return res