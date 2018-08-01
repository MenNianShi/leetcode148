class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = 0
        for i in range(len(num1)):
            val, carry = 0, 0
            for j in range(len(num2)):
                val *= 10
                tmp = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))
                val += tmp
            ans = 10*ans+val
        return str(ans)