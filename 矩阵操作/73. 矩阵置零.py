# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
#
# 示例 1:
#
# 输入:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
class Solution(object):
    """
    1、暴力法：设定一个同样大小的矩阵，每次遇到0，然后将第二个矩阵的相应位置置0，空间复杂度为O(mn)。



2、略微优化：每次遇到0的时候，记录需0的行号和列号，空间复杂度为O(m+n)。

 

3、空间复杂度为1，只需要将2中0的行号列号的记录在第一行和第一列就行了。

利用第一行和第一列的元素去标记该行或该列是否在更新时要全部变成0。但是这样操作会使得第一行和第一列的原始状态丢失。因此，我们需要额外一个变量hasZeros去保存第一列（或者第一行）在更新时是否要变成0，这样就不会有问题了。

    思路：不让用额外空间，那就用本身存储，首行存储对应列是否含0，首列（除了第一个）标识每一行是否含0，first标识第一行是否含0；
        1. 先标识
        2. 再修改:先将每行改为0，再将列改为0，再按first将第一行改为0
    """

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first = True
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        first = 0
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0

        for i in xrange(1, m):
            if matrix[i][0] == 0:
                matrix[i][:] = [0] * n
        for j in xrange(n):
            if matrix[0][j] == 0:
                for k in xrange(m):
                    matrix[k][j] = 0
        if not first:
            matrix[0][:] = [0] * n
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        r_set = set()
        c_set = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    r_set.add(i)
                    c_set.add(j)
        for i in r_set:
            for j in range(col):
                matrix[i][j] = 0
        for i in c_set:
            for j in range(row):
                matrix[i][j] = 0