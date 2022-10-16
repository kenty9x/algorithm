class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bsl(A, x): #Biany search left
            l, r = 0, len(A) - 1
            while l <= r:
                m = (l+r) / 2
                if x > A[m]: l = m+1
                else: r = m-1
            return l
        def bsr(A, x):
            l, r = 0, len(A) - 1
            while l <= r:
                m = (l+r) /2
                if x >= A[m]: l = m+1
                else: r = m - 1
            return r
        l, r = bsl(nums, target), bsr(nums, target)
        return (l, r) if l <= r else [-1, -1]