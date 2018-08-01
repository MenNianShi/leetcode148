# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        start = ListNode(0)
        start.next = head
        pre = start
        while pre.next:
            cur = pre.next
            while cur.next and (cur.next.val==cur.val):
                cur = cur.next
            if cur!=pre.next :
                pre.next = cur.next
            else:
                pre = pre.next
        return start.next