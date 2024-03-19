class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the maximum time is eating max(arr)
        # the minimum time can be 1
        # for every mid check if it is possible to finish at the required hour

        def helper(mid):
            ans=0
            for val in piles:
                ans+= ceil(val/mid)
            return ans<= h


        left, right= 1, max(piles)
        while left<= right:
            mid= (left+right)//2

            if helper(mid):
                right= mid-1
            else:
                left= mid+1
        
        return left 
