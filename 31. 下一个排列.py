# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#解题思路：输出字典序中的下一个排列。比如123生成的全排列是：123，132，213，231，312，321。
# 那么321的next permutation是123。下面这种算法据说是STL中的经典算法。
# 在当前序列中，从尾端往前寻找两个相邻升序元素，升序元素对中的前一个标记为partition。
# 然后再从尾端寻找另一个大于partition的元素，并与partition指向的元素交换，
# 然后将partition后的元素（不包括partition指向的元素）逆序排列。比如14532，
# 那么升序对为45，partition指向4，由于partition之后除了5没有比4大的数，所以45交换为54，即15432，
# 然后将partition之后的元素逆序排列，即432排列为234，则最后输出的next permutation为15234。确实很巧妙。
class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if len(num) <= 1: return
        partition = -1
        for i in range(len(num)-2, -1, -1):
            if num[i] < num[i+1]:
                partition = i
                break
        if partition == -1:
            num.reverse()
            return
        else:
            for i in range(len(num)-1, partition, -1):
                if num[i] > num[partition]:
                    num[i],num[partition] = num[partition],num[i]
                    break
        num[partition+1:len(num)]=num[partition+1:len(num)][::-1]
        return
a = Solution()
print(a.nextPermutation([1,3,2]))



