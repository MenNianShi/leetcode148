# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 示例 2:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        x = 0
        same = True
        for i in range(0,len(nums)-1):
            if nums[i]>nums[i+1]:
                x = i+1
                same =False
                break
        if same:
            return self.binsearch(nums,target)
        else:
            left = self.binsearch(nums[:x],target)
            right = self.binsearch(nums[x:],target)
            if left==-1 and right==-1:
                return -1
            if left!=-1:
                return left
            if right!=-1:
                return right+len(nums[:x])

    def binsearch(self,nums,target):
        left = 0
        right = len(nums)-1

        while left<=right:
            mid = (left + right) // 2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return -1
a  = Solution()
print(a.search([1,3],0))