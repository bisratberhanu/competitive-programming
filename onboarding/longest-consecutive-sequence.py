class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums.sort() #nlogn
        i=0
        counter=1
        ans=0
        while i< len(nums)-1:
            if nums[i]+1==nums[i+1]:
                counter+=1
            elif nums[i]==nums[i+1]:
                i+=1
                continue
            else:
                ans= max(ans,counter)
                counter=1
            i+=1
        ans= max(ans,counter)
        return ans 

