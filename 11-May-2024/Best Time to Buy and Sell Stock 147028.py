# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        maxprofit= -float('inf')
        left,right=0,1
        while right<len(prices):
            curprofit= prices[right]-prices[left]
            
            if curprofit>=0:
                maxprofit= max(maxprofit, curprofit)
              
            else:
                left=right
            right+=1
        if maxprofit<0: return 0
        else: return maxprofit 

        
        
        


            