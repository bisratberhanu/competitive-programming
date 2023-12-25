class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans=0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i-j==0:
                    ans+= mat[i][j]
                elif i+j== len(mat)-1 and i!=j:
                    ans+= mat[i][j]
        return ans 