class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        cur_digit = n
        res = []
        nums_disp = range(1,n+1)
        nk = k-1
        while cur_digit >= 1:
            cur_circ = math.factorial(cur_digit-1)
            cur_i = int(nk/cur_circ)
            res.append(nums_disp.pop(cur_i))
            cur_digit-=1
            nk = nk%cur_circ
        return ''.join([str(x) for x in res])