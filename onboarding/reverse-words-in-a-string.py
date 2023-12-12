class Solution:
    def reverseWords(self, s: str) -> str:
        lis= s.split()
        lis.reverse()
        return " ".join(lis)