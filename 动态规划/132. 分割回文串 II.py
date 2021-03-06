# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回符合要求的最少分割次数。
#
# 示例:
#
# 输入: "aab"
# 输出: 1
# 解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
# 可以通过动态规划解决，dp[i]表示字符串s[:i+1]需要的最少的切割次数，dp[i]的初始值为i，因为长度为i+1的字符串最多切割i次就能满足题目要求 。
# 当添加一个字符后，我们需要依次判断以它为末尾的子字符串是否是回文字符串，如果是，则要计算剩余字符串需要的最少切割次数加上一次是否能使当前的最少切割次数更少.
# 递推表达式如下：
#
# dp[i] = 0, 如果s[:i+1]是回文串
# dp[i] = min(dp[i], dp[j-1]+1), 如果s[j:i+1]是回文串

# 为了减少判断回文字符串时的计算，我们通过一个二维数组isPal[j][i]来缓存判断结果，isPal[j][i]表示字符串s[j:i+1]是否是回文字符串。
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0 for __ in range(n)]
        isPal = [[False for __ in range(n)] for __ in range(n)] # 是否回文存储矩阵
        for i in range(n):
            m = i
            for j in range(i + 1):  # j在左边开始，i右边
                if s[j] == s[i] and (j + 1 > i - 1 or isPal[j + 1][i - 1]):  # 如果i和j都不相等，不需要去判断是否是回文
                    isPal[j][i] = True
                    if j == 0:  # 整个都是回文串
                        m = 0
                    else:
                        m = min(m, dp[j - 1] + 1)  # 要么每个字母都拆，要么之前的字母拆了后+1
            dp[i] = m
        # for line in isPal:
        #     print line
        # print dp
        return dp[-1]
