import functools


class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        n = len(jobDifficulty)
        if n < d: return -1
        @functools.lru_cache(None)
        def dfs(i, d):
            if d == 1:
                return max(jobDifficulty[i:])
            res, maxd = float('inf'), 0
            for j in range(i, n - d + 1):
                maxd = max(maxd, jobDifficulty[j])
                res = min(res, maxd + dfs(j + 1, d - 1))
            return res
        return dfs(0, d)