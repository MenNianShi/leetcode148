# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
#
# 说明：
#
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 示例 2：
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
# 使用动态规划数组dp【】。
#
# 其中dp[i]是“以s[i]结尾的单词是否可以被字典中的单词拆分”。
#
# 返回值条件为dp【len（s）-1】是否为1（用1表示可以，0表示不可以）。
#
# 其中dp【i】=1的条件为：可以找到一个j，dp【j】=1 并且 s【j~i】存在于字典中，这就说明可以在j处进行拆分（拆分从0~i的子字符串）。
#
# 所以需要对前i-1项进行遍历。双重for循环。
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        return d[-1]