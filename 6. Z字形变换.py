# 将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"
#
# 实现一个将字符串进行指定行数变换的函数:
#
# string convert(string s, int numRows);
# 示例 1:
#
# 输入: s = "PAYPALISHIRING", numRows = 3
# 输出: "PAHNAPLSIIGYIR"
# 示例 2:
#
# 输入: s = "PAYPALISHIRING", numRows = 4
# 输出: "PINALSIGYAHRPI"
# 解释:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        zigzag = ['' for i in range(numRows)]  # 初始化zigzag为['','','']
        row = 0                                # 当前的行数
        step = 1                               # 步数：控制数据的输入
        for c in s:
            if row == 0:
                step = 1
            if row == numRows - 1:
                step = -1
            zigzag[row] += c
            row += step
        return ''.join(zigzag)