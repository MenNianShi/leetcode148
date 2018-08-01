# 给定一个未排序的整数数组，找出最长连续序列的长度。
#
# 要求算法的时间复杂度为 O(n)。
#
# 示例:
#
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 用一个字典存储中间值。遍历数组，对于数字i，找到i-1和i+1对应的value值,如果不存在则记0。
# 然后把i的value值设为i-1,i+1的value值之和，并加1，相当于连接起来。
# 同时置最左端和最右端的数的value值为i的value值（中间的数都已经出现过，不会再用到了）。然后更新一次最大值。
class Solution:
    """
    @param: num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        if num is None or len(num) == 0:
            return 0
        m = {}
        res = 0
        for i in num:
            if i not in m:
                l = 0
                r = 0
                if i - 1 in m:
                    l = m[i - 1]
                if i + 1 in m:
                    r = m[i + 1]
                m[i] = 1 + r + l
                m[i + r] = 1 + r + l
                m[i - l] = 1 + r + l
                res = max(res, m[i])
        return res