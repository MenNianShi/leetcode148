# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
#
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1:
#
# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
# 示例 2:
# 只允许做两次交易，这道题就比前两道要难多了。解法很巧妙，有点动态规划的意思：
#
# 开辟两个数组p1和p2，p1[i]表示在price[i]之前进行一次交易所获得的最大利润，
#
# p2[i]表示在price[i]之后进行一次交易所获得的最大利润。
#
# 则p1[i]+p2[i]的最大值就是所要求的最大值，
#
# 而p1[i]和p2[i]的计算就需要动态规划了，看代码不难理解。
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        n = len(prices)
        if n <= 1: return 0
        p1 = [0] * n
        p2 = [0] * n

        minV = prices[0]
        for i in range(1, n):
            minV = min(minV, prices[i])  # Find low and buy low
            p1[i] = max(p1[i - 1], prices[i] - minV)

        maxV = prices[-1]
        for i in range(n - 2, -1, -1):
            maxV = max(maxV, prices[i])  # Find high and sell high
            p2[i] = max(p2[i + 1], maxV - prices[i])

        res = 0
        for i in range(n):
            res = max(res, p1[i] + p2[i])
        return res