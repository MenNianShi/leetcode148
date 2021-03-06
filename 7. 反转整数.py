# 给定一个 32 位有符号整数，将整数中的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21
# 注意:
#
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        sign = 1
        if x < 0:
            sign = -1
        number = abs(x)
        sum = 0
        while number != 0:
            sum = sum*10 + number%10
            number //= 10
        result = sign*sum
        if result > 2147483647 or result < -2147483648:
            return 0
        return sign*sum
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        if x > 0:
            flag = 1
        else:
            flag = -1
        s = str(abs(x))[::-1]
        n = int(s) * flag
        return n if n.bit_length() < 32 else 0