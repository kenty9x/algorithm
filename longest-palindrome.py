class Solution(object):
    def expand_around_center(self, s, left, right):
        l = left
        r = right
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        return r - l - 1
    def longestPalindrome(self, s):
        if s == "":
            return ""
        start = end = 0
        for i in range(len(s)):
            len1 = self.expand_around_center(s, i, i)
            len2 = self.expand_around_center(s, i, i+1)
            len3 = max(len1, len2)
            if len3 > end - start:
                start = i - (len3 -1) /2
                end = i+ len3 /2
        return s[start:end+1]
        