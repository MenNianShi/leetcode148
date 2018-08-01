# 给定一个 n × n 的二维矩阵表示一个图像。
#
# 将图像顺时针旋转 90 度。
#
# 说明：
#
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
#
# 示例 1:
#
# 给定 matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]斜对称交换一下，竖对称交换一下结束
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix[0])
        for i in range(0,n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(0,n):
            for j in range(0,n//2):
                matrix[i][j],matrix[i][n-1-j]=matrix[i][n-1-j],matrix[i][j]

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        res = []
        n = len(matrix[0])
        for  c in range(0,n):
            l = []
            for r in range(n-1,-1,-1):
                l.append(matrix[r][c])
            res.append(l)
        matrix = res
        return matrix
a = Solution()
print(a.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))
