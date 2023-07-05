class Solution(object):
    memo = []
    def shortest_jump(self, nums, index):
        if index == -1:
            return self.memo[0] 
        if index == len(nums) -1:
            self.memo[index] = 0
        else:
            minimum = self.memo[index+1]
            for i in range(index+1, index+nums[index]+1, 1):
                if i >= len(nums):
                    break
                if self.memo[i] < minimum:
                    minimum = self.memo[i] 
            self.memo[index] = minimum + 1
        return self.shortest_jump(nums, index - 1)

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.memo = [10000]*len(nums)
        if len(nums) <= 1:
            return 0
        return self.shortest_jump(nums, len(nums)-1)
