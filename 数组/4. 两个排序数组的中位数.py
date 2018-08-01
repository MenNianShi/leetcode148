# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
#
# 请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 中位数是 2.0
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 中位数是 (2 + 3)/2 = 2.5
class Solution:
    def getKth(self,A,B,k):
        lenA = len(A)
        lenB = len(B)
        if lenA > lenB: return self.getKth(B, A, k)
        if lenA==0: return B[k-1]

        if k==1: return min(A[0],B[0])
        pa = min(k//2,lenA)
        pb = k-pa
        if A[pa-1]<=B[pb-1]:
            return self.getKth(A[pa:],B,pb)
        else:
            return self.getKth(A,B[pb:],pa)
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lenA = len(A)
        lenB = len(B)
        if (lenA+lenB)%2==1:
            return self.getKth(A,B,(lenA+lenB)//2+1)
        else:
            return (self.getKth(A,B,(lenA+lenB)//2)+self.getKth(A,B,(lenA+lenB)//2+1))*0.5