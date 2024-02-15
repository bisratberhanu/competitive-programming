class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        # GREEDY
        # the mas doubles should be used at large values as possible
        if target==1:
            return 0 
        ans=0
        for i in range(maxDoubles):
            if target%2==1:
                ans+=1
            target= target//2
            ans+=1
            if target== 1:
                return ans
        return ans+  target-1


