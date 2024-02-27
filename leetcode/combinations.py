class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def backTrack(n,k, temp,next):
            if len(temp)==k:
                ans.append(temp[:])
                return

            for i in range(next,n+1):
                temp.append(i)
                backTrack(n,k,temp, i+1)
                if temp:
                    temp.pop( )
        backTrack(n,k,[],1)
        
        return ans 
             
