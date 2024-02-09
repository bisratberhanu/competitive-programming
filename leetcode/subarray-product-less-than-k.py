class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<= 1: return 0
        product= 1
        ans,left=0,0
        for i in range(len(nums)):
            product*=nums[i]
            while product>=k:
                product//=nums[left]
                left+=1
            ans+= i-left+1
        return ans  
