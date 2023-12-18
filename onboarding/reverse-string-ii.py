class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans=''
        temp=''
        start=True
        i=0 
        while i< len(s):
            if (i+1)%(2*k)==0:
                start=True
                ans+= s[i]
            elif start and (i+1)%k!=0:
                temp+= s[i]
            elif (i+1)%k==0:
                temp+= s[i]
                temp= temp[::-1]
                ans+=temp
                start=False
                temp=''
            else:
                ans+= s[i]
            i+=1
        if temp:
            temp=temp[::-1]
            ans+=temp
        return ans 
        