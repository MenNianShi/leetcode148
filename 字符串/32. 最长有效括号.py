# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
# 示例 1:
#
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 示例 2:
#
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"  使用栈。这个解法比较巧妙，开辟一个栈，压栈的不是括号，而是未匹配左括号的索引！
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        last = -1
        maxlen = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)

            else:
                if len(stack) == 0:
                    last = i
                else:
                    stack.pop()
                    if len(stack) == 0:
                        maxlen = max(maxlen, i - last)
                    else:
                        maxlen = max(maxlen, i - stack[-1])

        return maxlen
a = Solution()
print(a.longestValidParentheses('(())'))