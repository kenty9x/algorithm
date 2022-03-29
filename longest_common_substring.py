def LCSubstr(string1, string2):
    m = len(string1)
    n = len(string2)
    # LCSuff is the table with zero value initially in each cell
    LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]

    # To store the length of longest common substring result = 0
    result = 0

    # Following steps to build LCSuff[m+1][n+1] in bottom up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                LCSuff[i][j] = 0
            elif (string1[i-1] == string2[j-1]):
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
    return result

print(LCSubstr("stringnay", "kiastring"))