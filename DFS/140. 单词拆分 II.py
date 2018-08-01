# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
#
# 说明：
#
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
#
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# 示例 2：
#
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
# 这道题不只像word break那样判断是否可以分割，而且要找到所有的分割方式，
# 那么我们就要考虑dfs了。不过直接用dfs解题是不行的，为什么？因为决策树太大，
# 如果全部遍历一遍，时间复杂度太高，无法通过oj。那么我们需要剪枝，如何来剪枝呢？
# 使用word break题中的动态规划的结果，在dfs之前，先判定字符串是否可以被分割，如果不能被分割，直接跳过这一枝。实际上这道题是dp+dfs。
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        Solution.res = []
        self.dfs(s, wordDict, '')
        return Solution.res

    def dfs(self, s, wordDict, stringlist):
        if self.check(s, wordDict):
            if len(s) == 0:
                Solution.res.append(stringlist[1:])
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    # print stringlist+' '+s[:i]
                    self.dfs(s[i:], wordDict, stringlist+' '+s[:i])

    def check(self, s, wordDict):
            dp = [False for i in range(len(s)+1)]
            dp[0] = True
            for i in range(len(s)):
                for j in range(i, -1, -1):
                    if dp[j] and s[j:i + 1] in wordDict:
                        dp[i + 1] = True
                        break
            return dp[len(s)]