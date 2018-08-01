# 给定一个二叉树
#
# struct TreeLinkNode {
#   TreeLinkNode *left;
#   TreeLinkNode *right;
#   TreeLinkNode *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:

            if root.left and root.right:
                root.left.next = root.right
                lastNode = root.right
            elif root.left: lastNode = root.left
            else: lastNode = root.right
            if lastNode:
                node = root.next
                while node:
                    if node.left:
                        lastNode.next = node.left; break
                    if node.right:
                        lastNode.next = node.right; break
                    node = node.next
            if root.right: self.connect(root.right)
            if root.left: self.connect(root.left)

