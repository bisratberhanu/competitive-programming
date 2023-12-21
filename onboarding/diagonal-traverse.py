class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic=defaultdict(list)
        ans=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dic[i+j].append(mat[i][j])
        for i in range(len(mat)+len(mat[0])-1):
            if i%2==0:
                dic[i].reverse()
                ans.extend(dic[i])
            else:
                #dic[i].reverse()
                
                ans.extend(dic[i])
        return ans 

                