# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 示例:
#
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#贪心算法求解
#     #（1）ret记录步数
#
# （2）last记录ret步数时，能走的最远距离
#
# （3）curr记录当前位置i能走的最远距离，为原curr和i+nums[i]的最大值
#
# （4）当位置i超越ret能走的last距离时，则需要增加一步ret+=1，并更新此步能走的最远距离last=curr
class Solution(object):
    # We use "last" to keep track of the maximum distance that has been reached
    # by using the minimum steps "ret", whereas "curr" is the maximum distance
    # that can be reached by using "ret+1" steps. Thus,curr = max(i+A[i]) where 0 <= i <= last.

    def jump(self, A):
        ret = 0
        last = 0
        curr = 0
        for i in range(len(A)):
            if i > last:
                last = curr
                ret += 1
            curr = max(curr, i + A[i])
        return ret
class Solution(object):#超时
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        self.steplist = []
        self.dfs(nums,0,len(nums)-1,0)

        return min(self.steplist)


    def dfs(self,nums,curindex,finalindex,step):
        if nums[curindex] == 0:
            return
        if curindex+nums[curindex]>=finalindex:
            step = step+1
            self.steplist.append(step)
            return
        else:

            for i in range(1,nums[curindex]+1):
                self.dfs(nums,curindex+i,finalindex,step+1)
a =Solution()
print(a.jump([2,0,2,0,1]))