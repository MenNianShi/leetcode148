#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid); n = len(obstacleGrid[0])
        res = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                res[i][0] = 1
            else:
                res[i][0] == 0
                break
        for i in range(n):
            if obstacleGrid[0][i] == 0:
                res[0][i] = 1
            else:
                res[0][i] = 0
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1: res[i][j] = 0
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[m-1][n-1]