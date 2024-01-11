class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        summ=0
        seen=set()
        left=0
        ans= float('-inf')
        for right in range(len(nums)):
            summ+= nums[right]
            
                
            while nums[right] in seen:
                seen.remove(nums[left])
                summ-=nums[left]
                left+=1
            seen.add(nums[right])
            ans= max(ans,summ)
        return ans 
                    
