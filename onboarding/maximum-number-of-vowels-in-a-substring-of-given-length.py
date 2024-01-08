class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels= ['a','e','i','o','u']
        left,right=0,0
        ans,vowel_counter=0,0
        while right<len(s):
            if right<=k-1:
                if s[right] in vowels:
                    vowel_counter+=1
                right+=1
                ans= max(ans,vowel_counter)
                continue
            if s[left] in vowels:
                vowel_counter-=1
            if s[right] in vowels:
                vowel_counter+=1
            left+=1
            right+=1
            ans= max(ans,vowel_counter)
        return ans 