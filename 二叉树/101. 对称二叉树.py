# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):#递归的方法
    # @param root, a tree node
    # @return a boolean
    def sym(self, left, right):
        if left == None and right == None:
            return True
        if left and right and left.val == right.val:
            return self.sym(left.left, right.right) and self.sym(left.right, right.left)
        else:
            return False

    def isSymmetric(self, root):
        if root == None:
            return True
        return self.sym(root.left, root.right)