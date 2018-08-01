#
# 给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        L = curs = ListNode(0)
        flag = 0

        while (l1 or l2 or flag):
            val1 = val2 = 0

            if (l1):
                val1 = l1.val
                l1 = l1.next

            if (l2):
                val2 = l2.val
                l2 = l2.next

            val = (val1 + val2 + flag) % 10
            flag = (val1 + val2 + flag) // 10

            curs.next = ListNode(val)
            curs = curs.next

        return L.next
class Solution:
    def addTwoNumbers(self, l1, l2):  #对短的链表后面补0，若长度一样break
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = False

        temp = ListNode(0)
        result = temp

        while l1!=None and l2!=None:
            if carry==True:

                curSum = l1.val + l2.val+1
            else:
                curSum = l1.val + l2.val
            if curSum >9:
                carry = True
            else:
                carry=False
            temp.next = ListNode(curSum%10)

            l1 = l1.next
            l2 = l2.next
            temp = temp.next
            if l1==None and l2 ==None:
                break
            if l1 ==None:
                l1 = ListNode(0)
            if l2 == None:
                l2 = ListNode(0)
        if carry==True:
            temp.next = ListNode(1)
        return result.next

l1 = ListNode(1)
p = ListNode(8)
l1.next = p
l2 = ListNode(0)
a = Solution()
print(a.addTwoNumbers(l1,l2))




