# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if not nums:
            return [[]]
        self.dfs(sorted(nums), [], ans)
        return ans

    def dfs(self, nums, cur, ans):
        if not nums:
            ans.append(cur)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                self.dfs(nums[:i] + nums[i + 1:], cur + [nums[i]], ans)


a = Solution()
print(a.permuteUnique([2,2,1,1]))