class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        parentheses = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                parentheses.append(i)
            else:
                parentheses.pop()
                if len(parentheses) == 0:
                    parentheses.append(i)
                else:
                    result = max(result, i - parentheses[-1])
                
        return result