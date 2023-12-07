class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=''
        hashm= set(spaces)
        for i in range(len(s)):
            if i in hashm:
                ans+=' '
                ans+=s[i]
            else:
              ans+=s[i]
        return ans 

