class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        insertIndex = 1
        for i in range(1,size):
            if nums[i-1] != nums[i]:
                nums[insertIndex] = nums[i]
                insertIndex += 1
        return insertIndex
    
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        insertIndex = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[insertIndex] = nums[i]
                insertIndex += 1
        return insertIndex
        