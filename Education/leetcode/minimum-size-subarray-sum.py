class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ=0
        left=0
        ans= float('inf')
        for right in range(len(nums)):
            summ+= nums[right]
            
         
            while summ>=target:
                
                ans=min(ans,right-left+1)
                summ-=nums[left]
                left+=1
        
        if ans==float('inf'): return 0
        return ans 