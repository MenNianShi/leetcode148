class Solution(object):
    def myPow(self, x, n):
        absn = n
        # if abs(x-0.0)<1e-6 and n<0:
        #     return 0.0
        if n < 0:
            absn = -n;
        result = self.power(x, absn)
        if n < 0:
            result = 1.0 / result
        return result

    def power(self, x, absn):
        if absn == 0:
            return 1
        elif absn == 1:
            return x
        result = self.power(x, absn >> 1)
        result *= result
        if (absn & 0x1):
            result *= x
        return result
