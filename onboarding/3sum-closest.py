class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=0
        minval= float('inf')
        for i,val in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r= i+1,len(nums)-1
            while l<r:
                threesum= nums[l]+nums[r]+val
                if abs(threesum-target)< minval:
                    minval= abs(threesum-target)
                    ans=threesum

                if threesum>target:
                    r-=1
                elif threesum< target:
                    l+=1
                else:
                    return threesum
        return ans 
                
                
        