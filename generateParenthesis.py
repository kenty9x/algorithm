class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(s=[],l=0,r=0):
            if len(s) == 2*n:
                ans.append("".join(s))
                return
            if l < n:
                s.append("(")
                backtrack(s,l+1,r)
                s.pop()
            if r<l:
                s.append(")")
                backtrack(s,l,r+1)
                s.pop()
        backtrack()
        return ans
    
    def generateParenthesis2(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for l in self.generateParenthesis2(c):
                for r in self.generateParenthesis2(n-1-c):
                    ans.append('({}){}'.format(l,r))
        return ans