# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
#
# 返回被除数 dividend 除以除数 divisor 得到的商。
#
# 示例 1:
#
# 输入: dividend = 10, divisor = 3
# 输出: 3
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor, div = abs(dividend), abs(divisor), abs(divisor)
        res = 0
        q = 1
        while dividend >= divisor:
                dividend -= div
                res += q
                q += q
                div += div
                if dividend < div:
                    div = divisor
                    q = 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)