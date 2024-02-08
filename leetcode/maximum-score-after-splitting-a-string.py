class Solution:
    def maxScore(self, s: str) -> int:
        def leftsum(string,index):
            ans=0
            for i in range(index+1):
                if string[i]=='0':
                    ans+= 1
            return ans 
        def rightsum(string,index):
            ans=0
            if index== len(string)-1:
                return float(-inf)
            for i in range(index+1,len(string)):
                ans+= int(string[i])
            return ans
        ans=float(-inf)
        for i in range(len(s)):
            temp= leftsum(s,i)+ rightsum(s,i)
            ans= max(ans,temp)
        return ans 