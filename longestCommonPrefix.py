class Solution(object):
    def commonPrefixUtil(self, str1, str2):
        result = ""
        n1 = len(str1)
        n2 = len(str2)
        i = j = 0
        while i <= n1 -1 and j <= n2 - 1:
            if str1[i] != str2[j]:
                break
            result += str1[i]
            i += 1
            j += 1
        return result
        
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for i in range(1, len(strs)):
            prefix = self.commonPrefixUtil(prefix, strs[i])
        return prefix        