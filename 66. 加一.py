# 给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 示例 2:
#
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        t = 0
        q = []
        for i in range(len(digits)):
            t = t * 10 + digits[i]
        t = t + 1

        while t != 0:
            m = t % 10
            q.append(m)
            t /= 10
        q = q[::-1]
        return q
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry =False
        if digits[-1]+1>9:
            carry=True
            digits[-1] = (digits[-1]+1)%10
        else:
            digits[-1]+=1
            return digits
        i=len(digits)-2
        while carry==True and i>=0:
            if digits[i] +1>9:
                carry=True
                digits[i] = (digits[i] + 1) % 10
                i=i-1
            else:
                carry=False
                digits[i] += 1
                return digits
        if i<0 and carry==True:

            digits.insert(0,1)
            return digits
a = Solution()
print(a.plusOne([9,9]))
