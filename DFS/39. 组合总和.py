# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
# 示例 2:
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
# 这个函数的主题逻辑是：
# Target =T，然后从数组中找一个数n，然后在 剩下的部分target 变成了 T-n，以此类推。
#
# 函数到哪返回呢，如果目标数T=0，则找的成功，返回，如果目标数T小于C中最小的数，言外之意就是我们找到不这样的组合了，寻找失败，返回。
# 需要注意的是，答案要求没有重复的，如果只是这么写会变成[2,3,2],[2,2,3]，[3,2,2]，因此要记下 上一个数，我是从小往大找的，也就是说，
#
# 如果我已经找完n=2的情况，再去找n=3的时候，3就不应该往回再选n=2了，只能往后走，不然就会重复。

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.resList = []
        candidates = sorted(candidates)
        self.dfs(candidates,[],target,0)
        return self.resList
    def dfs(self, candidates, sublist, target, last):
        if target == 0:
            self.resList.append(sublist[:])
        if target< candidates[0]:
            return
        for n in candidates:
            if n > target:
                return
            if n < last:
                continue
            sublist.append(n)
            self.dfs(candidates,sublist,target - n, n)
            sublist.pop()