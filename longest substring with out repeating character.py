class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = ''                             
        max_len = 0                 
        i = 0
        while i < len(s):
            if s[i] not in ss:         
                ss += s[i]
            else:
                ss = ss[ss.index(s[i])+1:] + s[i]     
                
            i += 1
            max_len = max(max_len, len(ss))     
        return max_len