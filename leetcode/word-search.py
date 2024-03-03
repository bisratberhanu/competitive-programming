class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dire= [(0,1), (1,0), (-1,0), (0,-1)]

        def backTrack(row,col,pos, seen):
            
            if pos== len(word)-1 and board[row][col]== word[-1] :
                
                return True 
            if pos>= len(word) or  board[row][col]!= word[pos]:
                
                return 
            for dx,dy in dire:
                xnew= dx+ row
                ynew= dy+ col

                if 0<= xnew < len(board) and 0<= ynew < len(board[0]) and (xnew,ynew) not in seen:
                    seen.add((xnew,ynew))
                    if backTrack(xnew, ynew,pos+1,seen):
                        return True
                    seen.remove((xnew,ynew)) 
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if len(word)==1 and board[i][j]== word[0]:
                    return True
                if len(word)==1: continue 
                seen= set()
                seen.add((i,j))
                if len(word)> 1 and backTrack(i,j,0, seen):
                    
                    return True
        return False
                 