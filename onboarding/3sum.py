class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i,val in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r= i+1, len(nums)-1
            while l<r:
                threesum= nums[l]+nums[r]+val
                if threesum>0:
                    r-=1
                elif threesum<0:
                    l+=1
                else:
                    ans.append([val,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return ans 
       

           
            
                