# 二叉搜索树中的两个节点被错误地交换。
#
# 请在不改变其结构的情况下，恢复这棵树。
#
# 示例 1:
#
# 输入: [1,3,null,null,2]
#
#    1
#   /
#  3
#   \
#    2
#
# 输出: [3,1,null,null,2]
#
#    3
#   /
#  1
#   \
#    2
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # 为Solution类添加数据成员precursor，用于在中序遍历树的过程中，指向当前节点的前驱节点。
        self.precursor = None
        ''' precursor初始值必须指定为None，随着不断的递归调用recursive_left_root_right()函数，
        precursor第一次被赋值指向二叉搜索树的最左节点（注意，不是最左叶节点。最左节点和最左叶节点可能不是同一个节点）'''

        # 为Solution类添加数据成员mistake1和mistake2，用于指向错误的两个节点
        self.mistake1 = None
        self.mistake2 = None
        self.recursive_left_root_right(root)  # 调用相应函数，找到错误的节点
        self.mistake1.val, self.mistake2.val = self.mistake2.val, self.mistake1.val  # 交换2个错误节点的值，使二叉搜索树恢复正常

    def recursive_left_root_right(self, root):
        if root == None:
            return
        self.recursive_left_root_right(root.left)  # 递归地中序遍历左子树

        if self.precursor != None and self.precursor.val > root.val:
            if not self.mistake1:
                self.mistake1, self.mistake2 = self.precursor, root
            else:
                self.mistake2 = root
        self.precursor = root

        self.recursive_left_root_right(root.right)  # 递归地中序遍历右子树
