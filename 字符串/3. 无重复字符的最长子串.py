# 给定一个字符串，找出不含有重复字符的最长子串的长度。
#
# 示例：
#
# 给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。
#
# 给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。
#
# 给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        hashTable = {}
        max_len = 0
        start = 0

        for i,c in enumerate(s):
            if c in hashTable :#and start <= hashTable[c] :
                start = hashTable[c] + 1  #当出现重复字符时，start变为该重复字符第一次出现位置的下一位
            else:
                max_len = max(max_len,i - start + 1)
            hashTable[c] = i

        return max_len
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='':
            return 0
        if len(s)==1:
            return 1
        maxlength = 0
        start = 0
        end = 1
        while end !=len(s):
            if s[end] not in s[start:end]:
                curLength = len(s[start:end+1])
                if curLength>maxlength:
                    maxlength = curLength
                end+=1
            else:
                start+=1
        return maxlength
