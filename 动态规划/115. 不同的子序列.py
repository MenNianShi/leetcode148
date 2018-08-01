# 给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。
#
# 一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
#
# 示例 1:
#
# 输入: S = "rabbbit", T = "rabbit"
# 输出: 3
# 解释:
#
# 如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)
#
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# 示例 2:
#
# 输入: S = "babgbag", T = "bag"
# 输出: 5
# 解释:
#
# 如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。
# (上箭头符号 ^ 表示选取的字母)
#
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^
# dp[i][j]表示字符串S[0:j] 中有多少个 T[0:i]
# 当i=2，j=6时，表示字符串 'babgbag' 中有多少个 'bag'，此时，要想知道现在有多少个'bag', 那么只需知道 j=5 时有多少个 'ba' 和已经有了多少个'bag', 接着再判断 S[j] ==T[i] 是否成立，如果成立，dp[i][j] = 'ba'的个数 + 已有'bag'的个数，dp[i][j] = 已有'bag'的个数。
#https://blog.csdn.net/XX_123_1_RJ/article/details/80789223
# 所以dp方程式为：dp[i][j] = dp[i][j-1] + dp[i-1][i-j] * (T[i] == S[j])（dp[i][j-1]对应绿色方格，dp[i-1][i-j]对应黄色方格）。
class Solution(object):
    def numDistinct(self, s, t):

        dp = [[0 for j in range(len(s)+1)] for i in range(len(t)+1) ]

        for j in range(len(s)+1):
            dp[0][j] = 1

        for i in range(len(t)):
            for j in range(len(s)):
                if t[i]==s[j]:
                    dp[i+1][j+1] = dp[i+1][j] + dp[i][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j]

        return dp[len(t)][len(s)]
# 由上图可知，我们按照一列一列的计算，后一列的值只和前一列的值相关，所以，现在我们只保留一列的dp，这样就可以又2维空间压缩到1维。

class Solution:
    def numDistinct(self, s, t):
        m, n = len(s) + 1, len(t) + 1
        dp = [0] * n  # 初始化dp
        dp[0] = 1

        for j in range(1, m):
            pre = dp[:]  # pre 表示前一列的值
            for i in range(1, n):
                dp[i] = pre[i] + pre[i - 1] * (t[i - 1] == s[j - 1])
        return dp[-1]
