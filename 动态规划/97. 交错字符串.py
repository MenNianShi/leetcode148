# 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
#
# 示例 1:
#
# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出: true
# 示例 2:
#
# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出: false
# DP[i][j]表示s1取前i位，s2取前j位，检查是否能组成s3的前i+j位。
# 如果新添加的字符，不等于s3里面对应的第（i+j）位，则取False。
# 若要取True，必须同时满足2个条件：
# 1》新添加的字符，要等于s3里面对应的第（i+j）位。
# 2》该格子的前一个格子也要等于True，为什么呢？我们举一个游戏的例子来形象的解释一下：在游戏中，通过一关为True,未通过为False。若第8关为True,则其前一关（第7关）必须也为True。因为若第7关为False，就 game over 了，根本就不会进入第8关，自然也不会取得第8关为True这样的结果。同理，若第7关为True，则第6关也必须为True，以此类推。。。
# https://blog.csdn.net/sxingming/article/details/51615358
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2)!=len(s3):
            return False
        DP=[[False]*(len(s2)+1) for i in range(len(s1)+1)]
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0 and j==0:
                    DP[i][j]=True
                elif i>0 and DP[i-1][j] and s3[i+j-1]==s1[i-1]:
                    DP[i][j]=True
                elif j>0 and DP[i][j-1] and s3[i+j-1]==s2[j-1]:
                    DP[i][j]=True
                else: #由于DP被初始化为全False，因此，该else语句可以省去
                    DP[i][j]=False
        return DP[len(s1)][len(s2)]