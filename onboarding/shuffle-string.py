class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        lis= [0]*len(s)
        for i in range(len(s)):
            lis[indices[i]]= s[i]
        return ''.join(lis)
              