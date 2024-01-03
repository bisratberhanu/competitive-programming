class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gptr=0
        sptr=0
        ans=0
        while sptr<len(s) and gptr<len(g):
            if g[gptr]<=s[sptr]:
                ans+=1
                gptr+=1
                sptr+=1
            else:
                sptr+=1
        return ans 