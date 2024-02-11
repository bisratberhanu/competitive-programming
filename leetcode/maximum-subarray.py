class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        acc=0
        minval= 0
        ans= float(-inf)
        for val in nums:
            acc+= val
            
            
            ans= max(ans,acc-minval)
            minval= min(minval,acc)
        return ans 
