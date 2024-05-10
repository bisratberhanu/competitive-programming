# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    # @cache
    def canPartition(self, nums: List[int]) -> bool:
        self.summ= sum(nums)  
        if self.summ % 2==1:
            return False
        casher= {}
        def dp(i,cursum):
            if (i,cursum) in casher:
                return casher[(i, cursum)]
            if self.summ//2 == cursum:
               return True
                
                 
            if i>= len(nums) or self.summ//2 < cursum :
                casher[(i,cursum)]= False
                return False 
            if dp(i+1, cursum + nums[i]):
                return True
            if dp(i+1, cursum):
                return True

            casher[(i,cursum)]= False 
            return False  
            
            
        
        return dp(0,0)
        
            