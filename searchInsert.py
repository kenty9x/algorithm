class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, h = 0, len(nums)-1
        while l < h:
            m = (l+h) // 2
            if (nums[m] < target):
                l = m + 1
            elif (nums[m] > target):
                h = m - 1
            else:
                return m
        if nums[l] >= target:
            return l
        else:
            return l+1