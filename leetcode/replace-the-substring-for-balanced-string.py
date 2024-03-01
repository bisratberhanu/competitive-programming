class Solution:
    def balancedString(self, s: str) -> int:
        # count the occurence outside the sliding window then if all values are less than n/4 
        # replacement can be done
        countdic= Counter(s)
        ans=float(inf)
        left=0
        n= len(s)
        for right in range(len(s)):
            countdic[s[right]]-=1
            while left < n and all(n/4>=countdic[c] for c in "QWER"):
                ans= min(ans, right-left+1)
                countdic[s[left]]+=1
                left+=1
            
            
        
        return ans 
            

         