class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        out = "1"
        for _ in range(n-1):
            tmp = ""
            cur = out[0]
            count = 0
            for i in out:
                if cur != i: 
                    tmp += str(count) + cur
                    cur = i
                    count = 1
                else:
                    count += 1
            
            if count: 
                tmp += str(count) + cur
            out = tmp
        return out