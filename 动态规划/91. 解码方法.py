# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
#
# 示例 1:
#
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 示例 2:
#
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

# 本题宜用动态规划：
#
# 共有三种情况：
#
# l  s[i-2]和s[i-1] 两个字符是10----26之间但不包括10和20这两个数时，有两种编码方式，比如23------>[“BC”，“W”]，所以dp[i] = dp[i-1]+dp[i-2]
#
# l  s[i-2]和s[i-1] 两个字符10或20这两个数时，有一种编码方式，比如10------>[“J”], 所以dp[i] = dp[i-2]
#
# l  s[i-2]和s[i-1] 两个字符不在上述两种范围时，编码方式为零，比如27，比如01，所以dp[i] = dp[i-1]

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" or s[0] == '0': return 0
        dp = [1, 1]
        for i in range(2, len(s) + 1):
            if 10 <= int(s[i - 2:i]) <= 26 and s[i - 1] != '0':  # 编码方式为2
                dp.append(dp[i - 1] + dp[i - 2])
            elif int(s[i - 2:i]) == 10 or int(s[i - 2:i]) == 20:  # 编码方式为1
                dp.append(dp[i - 2])
            elif s[i - 1] != '0':  # 编码方式为0
                dp.append(dp[i - 1])
            else:
                return 0
        # print(dp[len(s)])
        return dp[len(s)]

