# 假设你正在爬楼梯。需要 n 步你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 步 + 1 步
# 2.  2 步
# 示例 2：
#
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 步 + 1 步 + 1 步
# 2.  1 步 + 2 步
# 3.  2 步 + 1 步
class Solution:#递归复杂度太大
    def jumpFloor(self, number):
        # write code here
        if number<0:
            return -1
        if number==1 or number==2:
            return number
        else:
            return self.jumpFloor(number-1)+self.jumpFloor(number-2)

class Solution:  #循环代替递归
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n == 1 or n == 2:
            return n
        a = 1
        b = 2
        c = 3
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return c