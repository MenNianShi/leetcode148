# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
#
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 说明:
#
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 示例 1:
#
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出: 5
#
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#      返回它的长度 5。
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        wordList = set(wordList)
        forward, backward, n, cnt = {beginWord}, {endWord}, len(beginWord), 2
        dic = set(string.ascii_lowercase)

        while len(forward) > 0 and len(backward) > 0:
            if len(forward) > len(backward): # 加速
                forward, backward = backward, forward

            next = set()
            for word in forward:
                for i, char in enumerate(word):
                    first, second = word[:i], word[i + 1:]
                    for c in dic: # 遍历26个字母
                        candidate = first + c + second
                        if candidate in backward: # 如果找到了，返回结果，没有找到，则在wordList中继续寻找
                            return cnt

                        if candidate in wordList:
                            wordList.discard(candidate) # 从wordList中去掉单词
                            next.add(candidate) #加入下一轮的bfs中
            forward = next
            cnt += 1
        return 0