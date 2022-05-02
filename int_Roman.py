class Solution(object):
    def intToRoman(self, num):
        romans = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        idx = len(romans) - 1
        ans = ""
        while num > 0:
            while value[idx] <= num:
                ans += romans[idx]
                num -= value[idx]
            idx -= 1
        return ans
    def romanToInt(self, s):
        romans = {"I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000}
        n = len(s)
        num = romans[s[n-1]]
        for i in range(n -2, -1, -1):
            if romans[s[i]] >= romans[s[i+1]]:
                num += romans[s[i]]
            else:
                num -= romans[s[i]]
        return num
        
        