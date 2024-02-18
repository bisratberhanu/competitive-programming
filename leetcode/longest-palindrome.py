class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq= Counter(s)
        ans=0
        odd=0
        for val in freq:
            if freq[val]%2==0:
                ans+= freq[val]
            else:
                ans+= freq[val]-1
                odd= 1
        
        return ans + odd
