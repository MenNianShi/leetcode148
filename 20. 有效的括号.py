# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
# 示例 3:
#
# 输入: "(]"
# 输出: false
# 示例 4:
#
# 输入: "([)]"
# 输出: false
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack  = []

        for i in s:
            if i == '(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if stack==[]:
                    return False
                elif i==')' and stack[-1]=='(':
                    stack.pop(-1)
                elif i==']' and stack[-1]=='[':
                    stack.pop(-1)
                elif i=='}' and stack[-1]=='{':
                    stack.pop(-1)
                else:
                    return False
        if stack==[]:
            return True
        else:
            return False
a = Solution()
print(a.isValid("(])"))