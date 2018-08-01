
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 说明:
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution(object):
    def swapPairs(self, head):
        if head == None or head.next ==None:
            return head
        preNode = ListNode(0)
        preNode.next = head
        p = preNode
        while head!=None and head.next!=None:
            node1 = head
            node2 = head.next.next
            preNode.next = head.next
            preNode = preNode.next
            preNode.next = node1
            node1.next= node2
            preNode = preNode.next
            head = node2
        return p.next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next==None:
            return head
        temp = head.next
        head.next = self.swapPairs(temp.next)
        temp.next = head
        return temp
