class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefixsum=[0]*(len(nums)+1)
        res=[]
        for i in range(1,len(nums)+1):
            prefixsum[i]= prefixsum[i-1]+nums[i-1]
        for i in range(len(nums)):
            appended= nums[i]*i - prefixsum[i]
            nextappended= prefixsum[-1]- prefixsum[i] -((len(nums)-i)*nums[i])
            ans= appended+nextappended
            res.append(ans)
        return res 
        