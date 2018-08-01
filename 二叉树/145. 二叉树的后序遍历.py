class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [(root, False)] if root else []
        res = []
        while stack:
            root, flag = stack.pop()
            if flag:
                res.append(root.val)
            else:
                stack.append((root, True))
                if root.right: stack.append((root.right, False))
                if root.left: stack.append((root.left, False))
        return res


class Solution:

    def __init__(self):
        self.ret = []

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root != None:

            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.ret.append(root.val)

        return self.ret
