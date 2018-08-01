# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
# 示例:
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        word_dict = {}
        for i in strs:
            temp =sorted(i)
            temp = ''.join(temp)
            if temp not in word_dict:
                word_dict[temp]=[i]
            else:
                word_dict[temp].append(i)
        res = []
        for k,v in word_dict.items():
            res.append(v)
        return res
a = Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))