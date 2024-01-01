class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if min(costs)> coins:
            return 0
        costs.sort()
        acc=0
        ans=0
        for i in range(len(costs)):
            acc+= costs[i]
            if acc >coins:
                return ans
            
            
            ans+=1
        return ans
        