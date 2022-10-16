class Solution(object):
    f = open("demofile2.txt", "a")
    def isrowValid(self, board, row):
        l = []
        for i in board[row]:
            if i != ".":
                l.append(i)
        return len(set(l)) == len(l)
    
    def iscolValid(self, board, col):
        b = list(zip(*board))[col]
        l = []
        for i in b:
            if i != ".":
                l.append(i)
        return len(set(l)) == len(l)
            
    def isboxValid(self, board, row, col):
        r = row // 3
        c = col // 3
        l = []
        for i in range(3):
            for j in range(3):
                if board[i+r*3][j+c*3] != ".":
                    l.append(board[i+r*3][j+c*3])
        return len(set(l)) == len(l)
    
    def isValidSudoku(self, board, row, col):
        return self.isrowValid(board, row) and self.iscolValid(board, col) and self.isboxValid(board, row, col)
    
    def solveSudoku(self,board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if (i == 8 and j == 8):
                        return True
                    continue
                for trial in range(1,10):
                    board[i][j] = str(trial)
                    f.write(str(board))
                    f.write("\n")
                    if self.isValidSudoku(board, i, j):
                        if not self.solveSudoku(board):
                            board[i][j] = '.'
                        else:
                            return True
                    if trial == 9:
                        board[i][j] = "."
                        return False

         
f = open("demofile2.txt", "a")
print(Solution.solveSudoku(Solution(), [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
#print(Solution.solveSudoku(Solution(),[['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]))
f.close()