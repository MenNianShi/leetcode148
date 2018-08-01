class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0 for i in range(n)]for i in range(n)]
        direction_x = [1,0,-1,0]
        direction_y = [0,1,0,-1]
        index = [0,0]
        i = 0
        for j in range(1,n*n+1):
            result[index[0]][index[1]] = j
            if index[0] + direction_y[i] < 0 or index[0] + direction_y[i] > n - 1:
                i = (i + 1) % 4
            elif index[1] + direction_x[i] < 0 or index[1] + direction_x[i] > n - 1:
                i = (i + 1) % 4
            elif result[index[0] + direction_y[i]][index[1] + direction_x[i]] != 0:
                i = (i + 1) % 4
            index[0] = index[0] + direction_y[i]
            index[1] = index[1] + direction_x[i]
        return result
class Solution(object):
    def generateMatrix(self, n):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        matrix = [[0 for i in range(n)]for i in range(n)]
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
            matrix[iRow][iCol] = cnt + 1
            cnt += 1
            # print matrix[iRow][iCol]

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
        return matrix

a = Solution()
print(a.generateMatrix(3))