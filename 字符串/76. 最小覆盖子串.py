#
# 给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。
#
# 示例：
#
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
# 说明：
#
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
# 解这道题需要注意，t中的字符可能为重复字符，所以需要用字典记录每个字符出现的次数。
# 要判断窗口中是否出现了所有字符，首先需要左右指针表示窗口的位置
# ，同时要有另外一个字典记录窗口中每个字符出现的次数。另外一个变量记录窗口中t内的字符出现的次数。
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = len(t)
        minileft = 0
        miniSize = len(s) + 1
        left = 0
        cmap1 = {}
        cmap2 = {}
        for c in t:
            if c not in cmap1:
                cmap1[c] = 1
                cmap2[c] = 1
            else:
                cmap1[c] += 1
                cmap2[c] += 1

        for right in range(len(s)):
            if s[right] in cmap1:
                cmap2[s[right]] -= 1
                if cmap2[s[right]] >= 0:
                    count -= 1
                if count == 0:
                        while True:
                            if s[left] in cmap2:
                                if cmap2[s[left]] < 0:
                                    cmap2[s[left]] += 1
                                else:
                                    break
                            left += 1

                        if right - left + 1 < miniSize:
                            minileft = left
                            miniSize = right - minileft + 1

        if miniSize < len(s) + 1:
            return s[minileft:minileft + miniSize]
        else:
            return ''