#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
# 示例:
#
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3   dp[ n ] = 1/(n+1) * C(2n, n)

# 比如，以1为根的树有几个，完全取决于有二个元素的子树有几种。同理，2为根的子树取决于一个元素的子树有几个。以3为根的情况，则与1相同。
#
# 定义Count[i] 为以[0,i]能产生的Unique Binary Tree的数目，
#
# 如果数组为空，毫无疑问，只有一种BST，即空树，Count[0] =1
#
# 如果数组仅有一个元素{1}，只有一种BST，单个节点Count[1] = 1
#
# 如果数组有两个元素{1,2}， 那么有如下两种可能
#
# 1                       2
#   \                    /
#     2                1
# 1
# 2
# 3
# Count[2] = Count[0] * Count[1] (1为根的情况)
# + Count[1] * Count[0] (2为根的情况。
#
# 再看一遍三个元素的数组，可以发现BST的取值方式如下：
#
# Count[3] = Count[0]*Count[2] (1为根的情况)
# + Count[1]*Count[1] (2为根的情况)
# + Count[2]*Count[0] (3为根的情况)
#
# 所以，由此观察，可以得出Count的递推Count[i] = ∑ Count[0…k] * [ k+1….i] 0<=k
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]
        else:
            dp += [0 for i in range(n-2)]  # 后面创建多个
            for i in range(3, n + 1):
                for j in range(1, i+1):
                    # 若n为4：dp[0]*dp[3]+dp[1]*dp[2]+dp[2]*dp[1]+dp[3]*dp[0]
                    dp[i] += dp[j-1] * dp[i-j]
            return dp[n]