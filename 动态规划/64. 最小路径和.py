#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 首先找出递推关系，比如设存放起点到每个格子 i，j 的最小路径和的二维数组为 MPS[i][j]，递推公式为：
#
# MPS[i][j] = Min（MPS[i-1][j]，MPS[i][j-1]）+ grid[i][j]；
# 1
# 格子 i，j 的MPS值可能有两个来源：其左侧格子 i，j-1 或者其上侧格子 i-1，j ；
# 取这两个来源的较小MPS值，再加上当前格子的值 grid[i][j] 即为结果。！！！！
#
# 由于是从左上方向右下方走，故我们可以利用一个双重循环来进行迭代计算，
# 外层循环以行为单位，内层循环以列为单位，这样可以利用已经计算好的阶段 、状态来计算当前格子的结果，
# 因为每次计算某个格子时，其左侧格子和上侧格子结果已经算好，这也是动态规划比递归要快的原因
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    grid[i][j]=grid[i][j]
                elif i==0 or j==0:
                    if i==0: grid[0][j]+=grid[0][j-1]
                    else: grid[i][0]+=grid[i-1][0]
                else:
                    grid[i][j]=min(grid[i][j-1],grid[i-1][j])+grid[i][j]
        return grid[m-1][n-1]
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [0] * len(grid)
        # 任选一条路径，初始化距离
        dp[0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i] = dp[i - 1] + grid[i][0]
        for j in range(1, len(grid[0])):
            for i in range(len(grid)):
                dp[i] = min(dp[i], dp[i - 1]) + grid[i][j] if i > 0 else dp[i] + grid[i][j]
        return dp[len(grid) - 1]
