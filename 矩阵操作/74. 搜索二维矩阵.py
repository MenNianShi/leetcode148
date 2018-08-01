# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 示例 1:
#
# 输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
# 示例 2:
#
# 输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false
# 这道题也可以使用一次二分查找法，如果我们按S型遍历该二维数组，可以得到一个有序的一维数组，
# 那么我们只需要用一次二分查找法，而关键就在于坐标的转换，如何把二维坐标和一维坐标转换是关键点，
# 把一个长度为n的一维数组转化为m*n的二维数组(m*n = n)后，
# 那么原一维数组中下标为i的元素将出现在二维数组中的[i/n][i%n]的位置，有了这一点，代码很好写出来了。
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row,col=len(matrix),len(matrix[0])
        begin,end=0,row*col-1
        while begin<=end:
            mid=(begin+end)//2
            mid_value=matrix[mid/col][mid%col]
            if mid_value==target:
                return True
            elif mid_value<target:
                begin=mid+1
            elif mid_value>target:
                end=mid-1
        return False
class Solution(object):
    def binsearch(self,numList, target):
        low, high = 0, len(numList) - 1
        while low <= high:
            mid = (low + high) // 2
            if numList[mid] == target:
                return True
            elif numList[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False


    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        targetRow = 0
        for i in range(0, row - 1):
            if matrix[i][0] == target:
                return True
            elif target>matrix[i][0] and target<matrix[i+1][0] :
                targetRow = i
        if target == matrix[row-1][0]:
            return True
        if target > matrix[row-1][0]:
            targetRow = row -1
        return  self.binsearch(matrix[targetRow],target)


a = Solution()
print(a.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3))