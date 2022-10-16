class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(l-1,0,-1):
            if (nums[i] > nums[i-1]):
                for j in range(l-1,i-1,-1):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        tmp = nums[i:]
                        tmp.reverse()
                        for k in range(i,l,1):
                            nums[k] = tmp[k-i]
                        return
        nums.reverse()