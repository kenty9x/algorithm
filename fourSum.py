class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = set()
        nums.sort()
        n = len(nums)
        res = set()
        cur = [float('inf'),float('inf')]
        for i in range(n-3):
            if nums[i] == cur[0]:
                continue
            cur = [nums[i],float('inf')]
            for j in range(i+1, n-2):
                if nums[j] == cur[1]:
                    continue
                cur = [nums[i],nums[j]]
                lo, hi = j+1, n-1
                while (lo<hi):
                    if nums[i]+nums[j]+nums[lo]+nums[hi] == target:
                        output.add((nums[i],nums[j],nums[lo],nums[hi]))
                        lo += 1
                        hi -= 1
                    else:
                        mi = (lo + hi) // 2
                        if nums[i]+nums[j]+nums[lo]+nums[hi] > target:
                            if nums[i]+nums[j]+nums[lo]+nums[mi] > target and mi != lo and mi!= hi:
                                hi = mi
                            else:
                                hi -= 1
                        else:
                            if nums[i]+nums[j]+nums[mi]+nums[hi] < target  and mi!= lo and mi != hi:
                                lo = mi
                            else:
                                lo += 1
                        
        return output