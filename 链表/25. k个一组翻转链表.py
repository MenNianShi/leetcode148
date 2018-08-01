#
# 给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。
#
# 示例 :
#
# 给定这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:#https://www.cnblogs.com/asrman/p/3972325.html
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        # 迭代版，时间复杂度O(n)，空间复杂度O(1)
        # Need help
        if head == None: return head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy  # start =0.   Given this linked list: 1->2->3->4->5    #    For k = 2, you should return: 2->1->4->3->5
        while start.next:
            end = start  # end = 0
            for i in range(k - 1):
                end = end.next  # end = 1
                if end.next == None: return dummy.next
            (start.next, start) = self.reverse(start.next,
                                               end.next)  # (start.next=3, start=1)=self.reverse(start.next=1, end.next=2)
        return dummy.next

    def reverse(self, start, end):
        dummy = ListNode(0)
        dummy.next = start
        while dummy.next != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = dummy.next
            dummy.next = tmp
            # start.next, start.next.next, dummy.next = start.next.next, dummy.next, start.next
            # The above line is wrong! But WHY?
        return (end, start)
class Solution(object):
    def reverseKGroup(self, head, k):
        current_node = head
        count_node = 0
        while current_node and count_node != k:
            current_node = current_node.next
            count_node += 1
        if count_node == k:
            current_node = self.reverseKGroup(current_node, k)
            while count_node > 0:
                temp_node = head.next
                head.next = current_node
                current_node = head
                head = temp_node
                count_node -= 1
            head = current_node
        return head