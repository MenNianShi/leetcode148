# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, temp_result):
            if not nums:
                return
            else:
                value = "#"
                for i in range(len(nums)):
                    if nums[i] == value:  # 若同一层出现了上一次出现的元素则跳过
                        continue
                    else:
                        value = nums[i]  # 更新上一个元素值

                        # 不能用以下三行代码对temp_result进行更新和进行深度搜索，如果直接更新temp_result并作为深度搜索函数的参数，那么进行回溯的时候，就会混入之前添加的元素值，被深度搜索过程污染！！！
                        # temp_result.append(nums[i])
                        # result.append(temp_result)
                        # dfs(nums[i+1:], temp_result)

                        result.append(temp_result + [nums[i]])
                        dfs(nums[i + 1:], temp_result + [nums[i]])

        result = [[]]
        if nums == []:
            return result
        nums.sort()
        dfs(nums, [])
        return result