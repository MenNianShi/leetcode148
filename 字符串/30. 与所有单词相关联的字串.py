# 给定一个字符串 s 和一些长度相同的单词 words。在 s 中找出可以恰好串联 words 中所有单词的子串的起始位置。
#
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
#
# 示例 1:
#
# 输入:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# 输出: [0,9]
# 解释: 从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
# 示例 2:
#
# 输入:
#   s = "wordgoodstudentgoodword",
#   words = ["word","student"]
# 输出: []
# 因为words中的单词可能有重复，所以要有一个dict来记录一下每个字符串的数目。
# 然后在遍历原字符串的时候，只需要遍历单词的长度次即可，如”barfoothefoobarman”，因为目标单词的长度为3，所以只需遍历：
#
# ‘bar’ | ‘foo’ | ‘the’ | ‘foo’ | ‘bar’ | ‘man’
# ‘arf’ | ‘oot’ | ‘hef’ | ‘oob’ | ‘arm’
# ‘rfo’ | ‘oth’ | ‘efo’ | ‘oba’ | ‘rma’
# 在遍历时，需要两个指针，一个用来标记子字符串的开始，另一个用来标记子字符串的结束。
# 再用一个dict来记录当前字符串中单词的数量，如果下一个单词不在words中，那么清空该dict，把前指针直接跳到后指针处；
# 如果在words中，那么相应的键值要加一，此时如果那个单词的数量超过了目标中的数目，那么前指针要不断后移直到吐出一个那个单词。
# 通过前后指针之差是否等于所有目标单词长度之和来判断是否有目标子字符串。
import itertools
#words = ["foo","bar",'dsadsa']
#print(list(itertools.permutations(words, len(words))))
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s==''or words==[]:
            return []
        s_length = len(s)
        word_num = len(words)
        word_length = len(words[0])
        words_length = word_num * word_length
        result = []
        words_dict = {}
        for word in words:
            words_dict[word] = words_dict[word] + 1 if word in words_dict else 1
        for i in range(word_length):
            left = i
            right = i
            curr_dict = {}
            while right + word_length <= s_length:
                word = s[right:right + word_length]
                right += word_length
                if word in words_dict:
                    curr_dict[word] = curr_dict[word] + 1 if word in curr_dict else 1
                    while curr_dict[word] > words_dict[word]:
                        curr_dict[s[left:left + word_length]] -= 1
                        left += word_length
                    if right - left == words_length:
                        result.append(left)
                else:
                    curr_dict.clear()
                    left = right
        return result
class Solution(object):#超时
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s==''or words==[]:
            return []
        per_list = list(itertools.permutations(words, len(words)))
        words_list = []
        for i in per_list:
            temp = ''
            for j in i:
                temp= temp+j
            words_list.append(temp)
        #print(words_list)
        start = 0
        end = len(words_list[0])
        res = []
        while end<=len(s):
            x =s[start:end]
            if s[start:end] in words_list:
                res.append(start)
            start+=1
            end+=1
        return res
a = Solution()
print(a.findSubstring("barfoothefoobarman",["foo","bar"]))
