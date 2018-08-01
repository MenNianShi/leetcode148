# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 示例 2:
#
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):

    def rotateRight(self, head, k):

        """

        :type head: ListNode

        :type k: int

        :rtype: ListNode

        """

        if head == None or k == 0:
            return head

        dummy = ListNode(0)  # 创建一个虚假的头结点

        dummy.next = head  # 虚假头结点指向head

        # 计算链表长度

        count = 0

        p = dummy

        while p.next != None:
            p = p.next  # 最终P将指向尾节点

            count += 1

        p.next = dummy.next  # 将尾结点指向头结点，形成环形

        # 求真实的右移数量

        right = count - k % count

        p = dummy.next  # 指向head

        for i in range(1, right):  # i = 1 时，p为链表的第2个数据

            p = p.next

        head = p.next  # 移动后的头结点

        p.next = None

        return head
a = ListNode(1)
b = ListNode(2)
c =ListNode(3)
d =ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = None
v = Solution()
print(v.rotateRight(a,2))