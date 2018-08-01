# 给定一个二叉树，原地将它展开为链表。
#
# 例如，给定二叉树
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# 将其展开为：
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 方法一、后序遍历递归
class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root==None:return
        self.flatten(root.left)
        self.flatten(root.right)
        temp = root.right
        root.right = root.left
        root.left =None
        while root.right:
            root = root.right
        root.right = temp