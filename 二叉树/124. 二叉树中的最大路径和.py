# 给定一个非空二叉树，返回其最大路径和。
#
# 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
#
# 示例 1:
#
# 输入: [1,2,3]
#
#        1
#       / \
#      2   3
#
# 输出: 6
# 如果只是一个节点,那么当然就是这个节点的值了.
#
# 如果这个作为root,那么最长路应该就是..
#
# F(left) + F(right) + val...当然如果left,或者right<0就不用加了的= =
#
# 我盟从下往上找...
#
# 如果不这个不是root,那么就不能把left和right加起来了...因为只是一条路...
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ans = 0
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:return 0
        self.ans = root.val
        self.helper(root)
        return ans
    def helper(self,root):
        if root == None:return 0
        left  = self.helper(root.left)
        right = self.helper(root.right)
        val = root.val
        if left>0 : val+=left
        if right>0 : val+=right
        if val>self.ans : self.ans = val
        return max(root.val,max(root.val+left,root.val+right))

