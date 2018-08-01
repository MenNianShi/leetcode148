# 格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
#
# 给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。
#
# 示例 1:
#
# 输入: 2
# 输出: [0,1,3,2]
# 解释:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
#
# 对于给定的 n，其格雷编码序列并不唯一。
# 例如，[0,2,3,1] 也是一个有效的格雷编码序列。
#
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
# 示例 2:
#
# 输入: 0
# 输出: [0]
# 解释: 我们定义格雷编码序列必须以 0 开头。
#      给定编码总位数为 n 的格雷编码序列，其长度为 2n。当 n = 0 时，长度为 20 = 1。
#      因此，当 n = 0 时，其格雷编码序列为 [0]。

class Solution:
    # @param {int} n a number
    # @return {int[]} Gray code
    def grayCode(self, n):
        result = []
        if n == 0:
            return [0]
        for i in self.helper(n):
            result.append(int(i, 2))
        return result

    def helper(self, n):
        result = []
        if n == 1:
            return ["0", "1"]
        elif n > 1:
            result = self.helper(n - 1)
            index = len(result) - 1
            while index >= 0:
                temp = result[index]
                temp += "1"
                result.append(temp)
                result[index] += "0"
                index -= 1
        return result
