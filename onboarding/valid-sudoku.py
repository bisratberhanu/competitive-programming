class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row checking 
        
        for row in board:
            seen=set()
            for i in range(len(row)):
                if row[i]!='.' and row[i] in seen:
                    return False
                seen.add(row[i])
                #print(seen)
        print('rowtrue')
        # column checking
        for i in range(9):
            seen=set()
            for j in range(9):
                if  board[j][i]!='.' and board[j][i] in seen:
                    return False
                seen.add(board[j][i])
        print('colright')
        # the three by three matix checking
        for i in range(0,7,3):
            for j in range(0,7,3):
                #print(i,j)
                curmatrix= [board[i][j:j+3], board[i+1][j:j+3], board[i+2][j:j+3]]
                #print(curmatrix)
                seen= set()
                for row in curmatrix:
                    for temp in range(len(curmatrix)):
                        if row[temp]!= '.' and row[temp] in seen:
                            return False
                        seen.add(row[temp])
        return True 