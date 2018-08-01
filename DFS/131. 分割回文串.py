# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回 s 所有可能的分割方案。
#
# 示例:
#
# 输入: "aab"
# 输出:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res_lst = []
        if s is None or len(s) == 0:
            return res_lst
        self.dfs(s, [], res_lst, 0)
        return res_lst

    def dfs(self, s, pre_lst, res_lst, start):
        if start == len(s):
            res_lst.append(pre_lst[:])
            return
        for end in range(start, len(s)):
            if self.is_palindrome(s, start, end):
                pre_lst.append(s[start:end+1])
                self.dfs(s, pre_lst, res_lst, end+1)
                pre_lst.pop()

    @staticmethod
    def is_palindrome(s, start, end):
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
