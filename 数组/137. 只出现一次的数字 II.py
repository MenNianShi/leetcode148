#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
#
# 输入: [2,2,3,2]
# 输出: 3
# 示例 2:
#
# 输入: [0,1,0,1,0,1,99]
# 输出: 99
# 通过集合运算可以得到去除每个元素只出现一次的集合，计算集合和的3倍，减去原列表之和，即得到列表只出现一次的元素的两倍
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return  (sum(set(nums)) * 3 - sum(nums)) / 2
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        count = [0]*32
        for i in xrange(0,32):
            for num in nums:
                if num &(1<<i):
                    count[i] += 1
            if count[i] % 3 != 0:
                ret |= 1 << i
        if ret > 0x7fffffff:
            ret -=0x100000000
        return ret