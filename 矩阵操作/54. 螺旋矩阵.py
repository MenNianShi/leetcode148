# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1:
#
# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if 0 == len(matrix):
            return []

        rowMax = len(matrix) - 1
        rowMin = 0
        colMax = len(matrix[rowMax]) - 1
        colMin = 0
        numOfMatrix = (rowMax + 1) * (colMax + 1)

        x = [1, 0, -1, 0]  # row 方向的偏移值
        y = [0, 1, 0, -1]  # col 方向的偏移值
        direct = 0  # 0-right,1-down,2-left,3-up

        cnt = 0
        iRow = 0
        iCol = 0
        ans = []
        while cnt < numOfMatrix:
            cnt += 1
            # print matrix[iRow][iCol]
            ans.append(matrix[iRow][iCol])
            if direct == 0 and iCol == colMax:
                rowMin += 1
                direct = (direct + 1) % 4
            elif 1 == direct and iRow == rowMax:
                colMax -= 1
                # rowMax -= 1
                direct = (direct + 1) % 4
            elif 2 == direct and iCol == colMin:
                rowMax -= 1
                direct = (direct + 1) % 4
                # colMin += 1
            elif 3 == direct and iRow == rowMin:
                colMin += 1
                direct = (direct + 1) % 4
                # rowMin += 1

            iRow += y[direct]
            iCol += x[direct]
        return ans