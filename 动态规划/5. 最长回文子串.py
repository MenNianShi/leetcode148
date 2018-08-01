# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba"也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"
#
# 基本思路是对任意字符串，如果头和尾相同，那么它的最长回文子串一定是去头去尾之后的部分的最长回文子串加上头和尾。如果头和尾不同，那么它的最长回文子串是去头的部分的最长回文子串和去尾的部分的最长回文子串的较长的那一个。
# P[i,j]表示第i到第j个字符的回文子串数
# dp[i,i]=1
# dp[i,j]=dp[i+1,j−1]+2|s[i]=s[j]
# dp[i,j]=max(dp[i+1,j],dp[i,j−1])|s[i]!=s[j]


def longestPalindrome(s):
    n = len(s)
    maxl = 0
    start = 0
    for i in range(n):
        if i - maxl -1>= 0 and s[i - maxl - 1: i + 1] == s[i - maxl - 1: i + 1][::-1]:
            #i其实指向 已 判断出的回文串的下一个字符，比如abba，已判断到bb为回文串，maxl为2，i就指向bb的下一个字符a，i-2就指向第一个b，i-2-1就指向第一个a。
            #所以 s[i - maxl - 1: i + 1]  其实是包含 索引为 i-maxl-1的头，和索引为 i的尾

            start = i - maxl - 1
            maxl += 2
            continue
        if i - maxl >= 0 and s[i - maxl: i + 1] == s[i - maxl: i + 1][::-1]:
            #这里其实只包含了 索引为 i的尾

            start = i - maxl
            maxl += 1
    return s[start: start + maxl]
print(longestPalindrome('babab'))