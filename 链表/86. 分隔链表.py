#
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例:
#
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution(object):#把所有小于给定值的节点都移到前面，大于该值的节点顺序不变，相当于一个局部排序的问题。那么可以想到的一种解法是首先找到第一个大于或等于给定值的节点，用题目中给的例子来说就是先找到4，然后再找小于3的值，每找到一个就将其取出置于4之前即可
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        while pre.next and pre.next.val<x:
            pre = pre.next
        cur = pre
        while cur.next:
            if cur.next.val<x:
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
                pre = pre.next
            else:
                cur = cur.next
        return dummy.next
#构建两个新链表，小于x的放在链表1，大于或等于x的放在链表2，最后将链表1的表尾指向链表2的表头即可。
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        first = ListNode(None)
        f_cursor = first
        second = ListNode(None)
        s_cursor = second

        cursor = head
        while cursor is not None:
            if cursor.val < x:
                f_cursor.next = cursor
                f_cursor = f_cursor.next
            else:
                s_cursor.next = cursor
                s_cursor = s_cursor.next

            next_cur = cursor.next
            cursor.next = None
            cursor = next_cur

        f_cursor.next = second.next
        return first.next