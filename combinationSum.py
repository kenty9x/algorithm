class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        path = []
        def dfs(c, t, path, ret):
            if t < 0:
                return
            elif t == 0:
                ret.append(path)
            else:
                for i in range(len(c)):
                    dfs(c[i:], t-c[i], path+[c[i]], ret)
        dfs(candidates, target, path, ret)
        return ret
    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(comb, remain, curr, counter, results):
            if remain == 0:
                results.append(list(comb))
                return
            elif remain < 0:
                return
            
            for next_curr in range(curr, len(counter)):
                candidate, freq = counter[next_curr]
                if freq <= 0:
                    continue
                comb.append(candidate)
                counter[next_curr] = (candidate, freq-1)
                backtrack(comb, remain-candidate,next_curr,counter,results)
                counter[next_curr] = (candidate, freq)
                comb.pop()
        results = []
        counter = Counter(candidates)
        counter = [(c,counter[c]) for c in counter]
        backtrack([], target, 0, counter, results)
        return results