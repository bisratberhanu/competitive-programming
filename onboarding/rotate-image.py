class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ans=[]
        for i in range(len(matrix)):
            temp=[]
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            ans.append(temp)
        for row in ans:
            row.reverse()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j]= ans[i][j]
        
        