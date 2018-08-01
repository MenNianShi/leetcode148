# 对链表进行插入排序。
#
#
# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。
#
#
#
# 插入排序算法：
#
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
#
#
# 示例
# 1：
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 示例
# 2：
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 第一步：为了避免超时，要判断新结点是否有插入左边的必要，通过新结点与左边的邻结点比较，只有在值小于左边的邻结点才插入
# 第二步：从头结点开始，依次判断新结点插入位置，若新结点值比左边结点大，则p1指针右移。由于第一步比较，所以左边一定能找到比新结点大的结点。
# 第三步：找到新结点插入的位置，将新结点插入
# 注意：新结点插入时，需要将新结点赋予给临时结点，然后立即把新结点后面的结点拼接到新结点前一结点后，再将临时结点插入新位置，否则操作顺序一反会导致临时结点操作改变新结点后的结点！！！
# p1.next指针指向左边插入的位置，p2.next指向新的结点
class Solution(object):
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        dummy=ListNode(0)
        dummy.next=head
        p2=head
        while p2.next:
            if  p2.val>p2.next.val:
                p1=dummy
                while  p2.next.val>=p1.next.val:
                    p1=p1.next
                t=p2.next
                p2.next=p2.next.next
                t.next=p1.next
                p1.next=t
            else:
                p2=p2.next
        return  dummy.next

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        temp = []
        node = head
        while node != None:
            temp.append(node.val)
            node = node.next
        temp.sort()
        node = head
        for n in temp:
            node.val = n
            node = node.next
        return head

