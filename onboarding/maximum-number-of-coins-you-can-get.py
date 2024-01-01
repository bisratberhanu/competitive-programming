class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        ans=0
        for i in range(1,int(len(piles)*2/3),2):
            ans+= piles[i]
        return ans 
