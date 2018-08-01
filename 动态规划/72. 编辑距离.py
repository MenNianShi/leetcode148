# # 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
# #
# # 你可以对一个单词进行如下三种操作：
# #
# # 插入一个字符
# # 删除一个字符
# # 替换一个字符
# # 示例 1:
# #
# # 输入: word1 = "horse", word2 = "ros"
# # 输出: 3
# # 解释:
# # horse -> rorse (将 'h' 替换为 'r')
# # rorse -> rose (删除 'r')
# # rose -> ros (删除 'e')
# 【思路】
#
# l  替换：
#
# 若word1[i]替换为word2[j]是从word1到word2的最小改动，
# 则需先把word1[0至i-1]以最小距离变为word2[0至j-1]，然后在执行替换操作，此时res[i][j] = res[i-1][j-1] + 1
#
# l  插入：
#
# 若word1[i]插入某字符为是从word1到word2的最小改动，
# 则需先把word1[0至i-1]以最小距离变为word2[0至j-1]，然后在执行插入操作，此时res[i][j] = res[i-1][j-1] + 1
#
# l  删除：
#
# 若word1[i]删除某字符是从word1到word2的最小改动，
# 则需先把word1[0至i-1]以最小距离变为word2[0至j-1]，然后在执行插入操作，此时res[i][j] = res[i-1][j-1] + 1
class Solution:

    #@return an integer

    def minDistance(self, word1, word2):

       m=len(word1)+1

       n=len(word2)+1

       dp = [[0 for i in range(n)] for j in range(m)]#(m+1)*（n+1）二维矩阵

       for i in range(n):

           dp[0][i]=i

       for i in range(m):

           dp[i][0]=i

       for i in range(1,m):

           for j in range(1,n):

                dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1, dp[i-1][j-1]+(0 if word1[i-1]==word2[j-1] else 1))

       return dp[m-1][n-1]