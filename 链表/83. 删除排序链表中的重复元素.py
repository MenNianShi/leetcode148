# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
#
# 输入: 1->1->2
# 输出: 1->2
# 示例 2:
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3
class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #此为不带头结点的链表
        if head is None:#链表为空
            return head
        cur=head
        while cur.next:#下一节点不为空
            if cur.val==cur.next.val:#第一次判断，头元素与头元素下一节点的值是否相等。。。
                cur.next=cur.next.next
            else:
                cur=cur.next
        return head