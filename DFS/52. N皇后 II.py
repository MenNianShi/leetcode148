# 给定一个整数 n，返回 n 皇后不同的解决方案的数量。
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def DFS(queens,xy_diff,xy_sum):
            p=len(queens)
            if p==n:
                ans.append(queens)
                return
            #q表示新的皇后所在的列
            for q in range(n):
                if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                    DFS(queens+[q],xy_diff+[p-q],xy_sum+[p+q])
        ans=[]
        DFS([],[],[])
        return len(ans)
a = Solution()
print(a.totalNQueens(17))