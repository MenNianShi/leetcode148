# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 问总共有多少条不同的路径？
# 这是一道典型的动态规划问题，使用一个二维数组ans记忆到达每一点可行的走法总数。
# 首先将左边界点和上边界点初始化为1，因为机器人起始与（0，0），左边界点和上边界点的走法只有1种。接下来的每一点（x,y），
# 可以由（x-1，y）向右走或是（x,y-1）向下走来到达，因此在（x,y）这一点可到达的方法有ans[x-1][y]+ans[x][y-1]种，到达终点的方法则是ans最后一个点的数据。
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = [[1 for i in range(n)] for i in range(m)]
        print(d)
        for i in range(1,m):
            for j in range(1,n):
                d[i][j] = d[i-1][j] + d[i][j-1]
        print(d)
        return d[m-1][n-1]
a = Solution()
print(a.uniquePaths(3,7))
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        j=min(m-1,n-1)
        if j==0:
            return 1
        k=m+n-2
        res1=1
        res2=1
        for i in range(j):
            res1*=k-i
            res2*=j-i
        return res1/res2