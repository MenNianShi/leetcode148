# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个位置。
#
# 示例 1:
#
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
# 示例 2:
#
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。\
# 使用贪心算法，每次选择最远能达到的地方，假设从某一点最远可以到达A点，那么A点之前的所有点都是可以到达的。
# 所以我们只要不断的更新最远可达到的点，然后看是否最远的点超过了终点即可。
#
# 具体来说，就是根据A点之前所有的点加上其最远的距离，求它们的一个最大值，求到一个reach之后，迭代地求最大值即可。
class Solution(object):
    def canJump(self, nums):
        reach = nums[0]
        i = 0
        while i<len(nums) and i<=reach:
            reach = max(reach,i+nums[i])
            i += 1
        if reach>=len(nums)-1:
            return True
        else:
            return False
class Solution(object):#超时
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return True

        if self.dfs(nums,0,len(nums)-1)==True:
            return True
        return False




    def dfs(self,nums,curindex,finalindex):
        if nums[curindex] == 0:
            return
        if curindex+nums[curindex]>=finalindex:

            return True
        else:

            for i in range(1,nums[curindex]+1):
                if self.dfs(nums,curindex+i,finalindex)==True:
                    return True
a = Solution()
print(a.canJump([2,3,1,1,4]))