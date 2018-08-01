# 给定两个二进制字符串，返回他们的和（用二进制表示）。
#
# 输入为非空字符串且只包含数字 1 和 0。
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=int(a)
        b=int(b)
        c=self.decade2binary(self.binary2decade(a)+self.binary2decade(b))
        return str(c)

    def decade2binary(self,number):
        result = 0
        index=0
        while number:
            result = result +pow(10,index)* (number % 2)
            number = number / 2
            index+=1
        return result

    def binary2decade(self,number):
        index = 0
        result = 0
        while number:
            result = result + (number % 10) * pow(2, index)
            number = number / 10
            index+=1
        return result