class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            l = []
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in l:
                    l.append(board[i][j])
                else:
                    return False
        
        for k in range(3):
            for h in range(3):
                l = []
                for i in range(3):
                    for j in range(3):
                        if board[i+3*h][j+3*k] == ".":
                            continue
                        if board[i+3*h][j+3*k] not in l:
                            l.append(board[i+3*h][j+3*k])
                        else:
                            return False
        
        for j in range(len(board[0])):
            l = []
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in l:
                    l.append(board[i][j])
                else:
                    return False
        
        return True