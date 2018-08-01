# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
#Definition for singly-linked list.使用归并排序算法可将链表排序的时间复杂度缩减到的O(NlgN)
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists==None or len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        length = len(lists)
        mid = (length-1)//2
        l1 = self.mergeKLists(lists[:mid+1])
        l2 = self.mergeKLists(lists[mid+1:])
        return self.mergeTwoList(l1,l2)
    def mergeTwoList(self,l1,l2):
        newList = ListNode(0)
        p = newList
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 or l2

        return newList.next