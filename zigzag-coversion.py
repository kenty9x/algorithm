class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        ret = []
        n = len(s)
        cycleLen = 2*numRows - 2
        for i in range(numRows):
            j = 0
            while (j + i < n):
                ret.append(s[j+i])
                if i != 0 and i != numRows - 1 and j + cycleLen - i < n:
                    ret.append(s[j + cycleLen -i])
                j += cycleLen
        return "".join(ret)