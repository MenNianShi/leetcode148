# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 例如，给定三角形：
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 如果我们把数字都对应到数据在每一行中的下标上，可
# 以很容易发现，对于一个data[i][j]，和它相邻的数字就是data[i+1][j]和data[i+1][j+1]。这样一来问题就简单了
# 。假如我们用minimus[i][j]来表示从第i行第j列处的数字开始往下到最后一层的最小路径和，那么有
#
# minimus[i][j]=data[i][j]+min(minimums[i+1][j]+minimums[i+1][j+1])
# 然而上述描述中需要一个O（n^2）的额外空间，接下来我们来解决这个问题。
#
# 由于我们在公式里需要递归求解子问题，那么我们不妨反过来想一下，先求解子问题，
# 然后再解决父问题。即，从下往上求解最小路径和。我们可以发现如下规律，
# 当我们求解minimum[i][j]时，我们会用到minimum[i+1][j]和minimum[i+1][j+1]，
# 但是当求解完所有minimum[i]之后minimum[i+1]就没有用处了。
# 既然如此，我们是否可以复用同一个空间来存储minimum的值呢？答案是可以的。
# 进一步观察发现，存储最后一行的每个数字的最小路径和需要n个空间>，
# 因此至少我们需要n个空间，这也是题目里给出O（n）的空间复杂度的原因；
# 之后存储倒数第二行时，我们只需要前面的n-1个空间……以此类推，第一行只需要一个空间来存储最小路径和，这也正是我们要求解的结果。
class Solution:
    def minimumTotal(self, triangle):
        f = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in range(len(row)):
                f[i] = row[i] + min(f[i], f[i + 1])
        return f[0]