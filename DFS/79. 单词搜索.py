# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 示例:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.
class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(x, y, word):
            if len(word) == 0:  # 说明所有字母均在单词板上找到
                return True
            # up
            if x > 0 and board[x - 1][y] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x - 1, y, word[1:]):
                    return True
                board[x][y] = tmp
            # down
            if x < len(board) - 1 and board[x + 1][y] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x + 1, y, word[1:]):
                    return True
                board[x][y] = tmp
            # left
            if y > 0 and board[x][y - 1] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x, y - 1, word[1:]):
                    return True
                board[x][y] = tmp
            # right
            if y < len(board[0]) - 1 and board[x][y + 1] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x, y + 1, word[1:]):
                    return True
                board[x][y] = tmp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:  # 首字母相等的位置
                    if (dfs(i, j, word[1:])):  # 寻找下一个字母是否在单词板
                        return True

        return False