# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。

strs = ["flower","flow","flight"]
print(min(len(i) for i in strs))

s = 'sdsdsds'
print(s[:-1])
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ''
        prefix = strs[0]

        # iterate for all strings
        for i in range(1, len(strs)):

            # at any point of time, if the prefix breaks, backtrack (trim right the prefix by one)
            # prefix 变化过程：flower ->flowe  ->flow ->flo ->fl
            while strs[i][:len(prefix)] != prefix:
                prefix = prefix[:-1]
        return prefix
a = Solution()
print(a.longestCommonPrefix(["flower","aa","flight"]))

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minlen = min(len(i) for i in strs)
        start = 0
        res = ''
        for i in range(0,minlen):
            temp = strs[0][i]
            for j in range(0,len(strs)):
                if strs[j][i]!=temp:
                    return res
            res =res+temp
        return res
