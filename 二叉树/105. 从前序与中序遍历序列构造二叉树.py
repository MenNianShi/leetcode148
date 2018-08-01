# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder,inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        else:
            res = TreeNode(preorder[0])
            res.left = self.buildTree(preorder[1: inorder.index(preorder[0]) + 1], inorder[: inorder.index(preorder[0])])
            res.right = self.buildTree(preorder[inorder.index(preorder[0]) + 1: ], inorder[inorder.index(preorder[0]) + 1: ])
        return res


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preindex = 0  # 先序遍历的下标
        ind = {v: i for i, v in enumerate(inorder)}  # 中序遍历{值:下标}
        head = self.dc(0, len(preorder) - 1, preorder, inorder, ind)
        return head

    def dc(self, start, end, preorder, inorder, ind):
        if start <= end:
            mid = ind[preorder[self.preindex]]  # 找到当前先序点对应的中序下标
            self.preindex += 1  # 遍历下一个
            root = TreeNode(inorder[mid])  # 当前根节点
            root.left = self.dc(start, mid - 1, preorder, inorder, ind)
            root.right = self.dc(mid + 1, end, preorder, inorder, ind)
            return root