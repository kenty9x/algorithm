class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        l = [["a","b","c"],["d","e","f"],["g","h","i"],
             ["j","k","l"],["m","n","o"],["p","q","r","s"],
             ["t","u","v"],["w","x","y","z"]]
        output = []
        for i in digits:
            tmp = list(output)
            output = []
            if len(tmp) == 0:
                for j in l[int(i) - 2]:
                    output.append(j)
            else:
                for k in tmp:
                    for j in l[int(i) - 2]:
                        output.append(k+j)
        return output