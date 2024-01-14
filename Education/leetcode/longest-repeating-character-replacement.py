class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans= float(-inf)
        dic= Counter(s)
        for val in dic:
            letter= val
            left=0
            counter=0
            for right in range(len(s)):
                if s[right]!= letter:
                    counter+=1
                while counter>k:
                    if s[left]!= letter:
                        counter-=1
                    left+=1
                ans= max(ans, right-left+1)
        return ans 
