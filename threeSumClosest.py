class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        diff = float('inf')
        n = len(nums)
        nums.sort()
        for i,num in enumerate(nums):
            lo, hi = i + 1, n - 1
            while(lo < hi and diff != 0):
                total = num + nums[lo] + nums[hi]
                if abs(target-total) < abs(diff):
                    diff = target - total
                mi = (hi + lo)//2
                if total > target:
                    if mi != hi and nums[mi] + num + nums[lo] > target:
                        hi = mi
                    else:
                        hi -= 1
                elif total < target:
                    if mi != lo and nums[mi] + num + nums[hi] < target:
                        lo = mi
                    else:
                        lo += 1
                    lo += 1
                else:
                    return target
        return target - diff