class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

       if len(nums)== 1:
           return nums[0] 
       left,right=1,k
       init_sum= sum(nums[0:k])
       ans= init_sum/k
       while right<len(nums):
           init_sum-=nums[left-1]
           init_sum+=nums[right]
           ans= max(ans,init_sum/k)
           left+=1
           right+=1
       return ans 
