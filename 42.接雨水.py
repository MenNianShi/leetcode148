class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trap(self, A):
        # write your code here
        n = len(A)
        if (n <= 2):
            return 0
        max = -1
        maxInd = 0
        for i in range(n):
            if A[i] > max:
                max = A[i]
                maxInd = i
        leftMax = A[0]
        area = 0
        for i in range(maxInd):
            if leftMax < A[i]:
                leftMax = A[i]
            else:
                area = area + leftMax - A[i]

        rightMax = A[n - 1]
        for i in range(n - 1, maxInd, -1):
            if rightMax < A[i]:
                rightMax = A[i]
            else:
                area = area + rightMax - A[i]

        return area
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0

        left  = 0
        right  = len(height) -1
        maxv = 0
        while left < right:
            if height[left] > height[right]:
                vm = height[right]
                right -=1
                while height[right] <vm and left < right:
                    maxv = maxv+vm-height[right]
                    right -=1
            else:
                vm = height[left]
                left +=1
                while height[left] < vm and left < right:
                    maxv = maxv+vm-height[left]
                    left +=1
a = Solution()
print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))