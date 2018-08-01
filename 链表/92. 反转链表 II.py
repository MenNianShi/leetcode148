# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        fake = ListNode(0)
        fake.next = head
        cur = head
        prev = fake
        length = n - m
        for _ in range(m-1):
            prev = prev.next
            cur = cur.next
        last = cur
        for _ in range(length+1):
            next = cur.next
            cur.next = prev.next
            prev.next = cur
            cur = next
        last.next = cur
        return fake.next