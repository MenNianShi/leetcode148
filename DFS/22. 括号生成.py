# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
# 思路：合法的情况是，任意一时刻，左（“(”）括号数要大于等于右（")"）括号数。关键在于题中只给了括号的对数，没有形象的左右括号字符，如何在脑海中转过弯去解题。故，在某次的调用中，
#
# 1）left大于right（left和right分别表示剩余左右括号的个数），即，临时变量中右括号的数大于左括号的数，则说明出现了“)(”，这是非法情况，返回即可；
#
# 2）left和right都等于0说明，临时变量中左右括号数相等，所以将临时变量中的值存入res中；
#
# 3）其余的情况是，先放左括号，然后放右括号，然后递归。注意参数的更新。
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res =[]
        self.DFS(n,n,'',res)
        return res

    def DFS(self,left,right,temp,res):
        if left>right:
            return
        if left==0 and right==0:
            res.append(temp)
        else:
            if left>0:
                self.DFS(left-1,right,temp+'(',res)
            if right>0:
                self.DFS(left,right-1,temp+')',res)
