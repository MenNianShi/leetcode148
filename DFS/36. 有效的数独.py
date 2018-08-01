class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dic_row = [{},{},{},{},{},{},{},{},{}]
        dic_col = [{},{},{},{},{},{},{},{},{}]
        dic_box = [{},{},{},{},{},{},{},{},{}]

        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num == ".":
                    continue
                if num not in dic_row[i] and num not in dic_col[j] and num not in dic_box[3*(i//3)+(j//3)]:
                    dic_row[i][num] = 1
                    dic_col[j][num] = 1
                    dic_box[3*(i//3)+(j//3)][num] = 1
                else:
                    return False

        return Tru
#最直观的思路，三个规则全部检查一遍即可。
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            if not self.isValidNine(board[i]):
                return False
            col = [c[i] for c in board]
            if not self.isValidNine(col):
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                block = [board[s][t] for s in [i, i+1, i+2] for t in [j, j+1, j+2]]
                if not self.isValidNine(block):
                    return False
        return True

    def isValidNine(self, row):
        map = {}
        for c in row:
            if c != '.':
                if c in map:
                    return False
                else:
                    map[c] = True
        return True