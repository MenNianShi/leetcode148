# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
#
# 示例:
#
# 输入: 3
# 输出:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# 解释:
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
# 对于求数量的题目一般考虑DP，而枚举所有符合条件的情况，一般用DFS。每次选取其中一个为根结点，然后求左右子树。当输入n时，二叉查找树由【1, 2，···i,···n】构成
#
# 根据二叉查找树的构成性质：当选择i为根结点时，【1, 2，···i - 1】构成其左子树，【i + 1, i + 2,···，n】构成其右子树。
#
# 当b > e时，返回空(注意不是null)；
# 当b <= e时，用leftTree  和rightTree来分别接收左右子树。
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1, n)

    def dfs(self, b, e):  # b,e为开始和结束数字
        if b > e:
            return [None]
        res = []
        for rootVal in range(b, e + 1):
            leftTree = self.dfs(b, rootVal - 1)
            rightTree = self.dfs(rootVal + 1, e)
            for i in leftTree:
                for j in rightTree:
                    root = TreeNode(rootVal)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res
