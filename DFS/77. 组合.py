# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
class Solution(object):#堆栈
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1
class Solution(object):#DFS
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res_lst = []
        if n == 0 or k == 0 or k > n:
            return res_lst
        self.dfs(list(range(1, n+1)), [], k, res_lst)
        return res_lst

    def dfs(self, nums, pre_lst, k, res_lst):
        if k == 0:
            res_lst.append(pre_lst[:])
            return
        if len(nums) < k:
            return
        for i in range(len(nums)):
            pre_lst.append(nums[i])
            if i == len(nums) - 1:
                self.dfs([], pre_lst, k-1, res_lst)
            else:
                self.dfs(nums[i+1:], pre_lst, k-1, res_lst)
            pre_lst.pop()

import itertools
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return list(itertools.combinations(range(1,n+1),k))