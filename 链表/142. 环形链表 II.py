# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 说明：不允许修改给定的链表。
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, pHead):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if pHead==None or pHead.next==None or pHead.next.next==None:
            return None
        low=pHead.next
        fast=pHead.next.next
        while low!=fast:
            if fast.next==None or fast.next.next==None:#说明无环
                return None
            low=low.next
            fast=fast.next.next
        #如果走出上面这个循环说明有环，且fast = slow
        fast=pHead
        #找出环的入口
        while low!=fast:
            low=low.next
            fast=fast.next
        return fast