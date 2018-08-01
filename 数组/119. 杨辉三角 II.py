# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #if rowIndex==0:return [1]
        ans=[1 for i in range(rowIndex+1)]
        for i in range(1,rowIndex+1):
            for j in range(i-1,0,-1):
                ans[j]=ans[j-1]+ans[j]
        return ans