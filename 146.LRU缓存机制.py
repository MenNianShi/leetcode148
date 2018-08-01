# LRUCache全名为Least Recently Used，即最近最少使用算法，是操作系统中发生缺页中断时常用的一种页面置换算法。
#
# 根据局部性原理，最近使用的数据块很有可能继续被频繁使用，因此当Cache已满的时候，LRUCache算法会把最久未使用的数据块替换出去。
#
# 对于LRU算法主要实现两个操作：
#
# 访问数据块
# 将访问的数据块更新为最近访问，并返回访问的数据块。
# 添加数据块
# 如果Cache还有容量，将添加的数据块添加到Cache之后标记为最近访问。
# 如果Cache的容量已满，替换最久未访问的数据块为添加的数据块。
class ListNode(object):
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.v2n = {}
        self.n2v = {}
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.v2n:
            node = self.v2n[key]
            if self.head.next is not node:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.next = self.head.next
                self.head.next.prev = node
                node.prev = self.head
                self.head.next = node
            return node.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.v2n:
            node = self.v2n[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head.next
            self.head.next.prev = node
            node.prev = self.head
            self.head.next = node
        else:
            if self.capacity == 0:
                delete_node = self.tail.prev
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev
                delete_key = self.n2v[delete_node]
                del self.n2v[delete_node]
                del self.v2n[delete_key]
                self.capacity += 1
            node = ListNode(value)
            self.v2n[key] = node
            self.n2v[node] = key
            node.next = self.head.next
            self.head.next.prev = node
            node.prev = self.head
            self.head.next = node
            self.capacity -= 1