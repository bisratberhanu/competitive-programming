class Solution:
    def printVertically(self, s: str) -> List[str]:
        lis= s.split()
        ans=[]
        
        largest_len=0
        for word in lis:
            
            largest_len= max(largest_len,len(word))
        for i in range(largest_len):
            temp=''
            for j in range(len(lis)):
                if i>=len(lis[j]):
                    temp+=' '
                else:
                    temp+= lis[j][i]
            temp= temp.rstrip()
            ans.append(temp)
        return ans 