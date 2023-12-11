class Solution:
    def freqAlphabets(self, s: str) -> str:
        def helper(string):
            
            return chr(ord('a')+int(string)-1)
        ans=''
        counter=0
        i=0
        while i<len(s):
            if i<len(s)-2 and s[i+2]=='#':
                ans+=helper(s[i]+s[i+1])
                i+=2
            else:
                ans+= helper(s[i])
            i+=1
        return ans 
            


    
