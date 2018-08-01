# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# #
# # candidates 中的每个数字在每个组合中只能使用一次。
# #
# # 说明：
# #
# # 所有数字（包括目标数）都是正整数。
# # 解集不能包含重复的组合。
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []

        candidates = sorted(candidates)
        self.dfs(candidates,target,[],0)
        return self.res
    def dfs(self,candiates,target,sublist,index):
        if target ==0:
            self.res.append(sublist)
            return
        else:
            for i in range(index,len(candiates)):
                if i>index and candiates[i]==candiates[i-1]:
                    continue
                temp = target-candiates[i]
                if temp>=0:
                    self.dfs(candiates,temp,sublist+[candiates[i]],i+1)
                else:
                    return


b = [10,1,2,7,6,1,5]
c = 8
a = Solution()
print(a.combinationSum2(b,c))