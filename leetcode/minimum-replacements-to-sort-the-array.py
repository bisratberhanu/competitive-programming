class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        #greedy
        '''bucket is ceil(nums[i]/nums[i+1]) 4/bucket is the optimal at pos just behind, '''
        ans= 0
        lastval= nums[-1]
        for i in range(len( nums)-2,-1,-1):
            if nums[i] >lastval:
                bucket= ceil(nums[i]/lastval)
                ans+= bucket-1
                lastval= nums[i]//bucket
            else:
                lastval= nums[i]
        return ans 
