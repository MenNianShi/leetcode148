# 给定一个没有重复数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        sub = []
        self.dfs(nums,sub)
        return self.result

    def dfs(self,nums,subList):
        if len(subList) == len(nums):
            self.result.append(subList[:])
        for num in nums:
            if num in subList:
                continue
            subList.append(num)
            self.dfs(nums,subList)
            subList.remove(num)
a = Solution()
print(a.permute([1,3,2]))
import itertools
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = list(itertools.permutations(nums))
        return s