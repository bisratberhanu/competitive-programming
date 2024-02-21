class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex== 1:
            return [1,1]
        
        prevrow= self.getRow(rowIndex-1)
        ans= [1]
        for i in range(len(prevrow)-1):
            ans.append( prevrow[i]+ prevrow[i+1])
        ans.append(1)
        return ans 