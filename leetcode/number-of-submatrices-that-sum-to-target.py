class Solution:
    def prefix(self, matrix: List[List[int]]):
            
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == 0:
                    if col != 0:
                        matrix[row][col] += matrix[row][col-1]
                elif col == 0:
                    matrix[row][col] += matrix[row-1][col]
                else:
                    matrix[row][col] += (matrix[row][col-1]+matrix[row-1][col]-matrix[row-1][col-1])
        return matrix

    
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        matrix= self.prefix(matrix)
    
        ans=0
        for r1 in range(len(matrix)):
            for r2 in range(r1, len(matrix)):
                dic= defaultdict(int)
                dic[0]=1
                for c in range(len(matrix[0])):
                    
                    cur_sum=  matrix[r2][c]- ( matrix[r1-1][c] if r1>0 else 0)
                    ans+= dic[cur_sum-target]
                    dic[cur_sum]+=1
        return ans 


        