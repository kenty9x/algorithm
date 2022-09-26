class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        d = {}
        nums.sort()
        cur = -1000000
        for i in range(len(nums)-1):
            # Find all pairs with sum
            # equals to "-arr[i]"
            if nums[i] == cur:
                continue
            s = set()
            for j in range(i+1, len(nums)):
                x = -(nums[i]+nums[j])
                if x in s:
                    tmp = [nums[i], x, nums[j]]
                    if str(tmp) not in d:
                        d[str(tmp)] = 1
                        result.append(tmp)
                else:
                    s.add(nums[j])
            cur = nums[i]
        return result