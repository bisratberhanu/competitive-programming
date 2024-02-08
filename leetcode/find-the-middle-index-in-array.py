class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefixsum=[0 for _ in range(len(nums)+1)]
        for i in range(1,len(nums)+1):
            prefixsum[i]= prefixsum[i-1]+nums[i-1]
        
        for i in range(len(nums)):
            temp1 = prefixsum[i]
            temp2= prefixsum[-1]- prefixsum[i+1]
            if temp1==temp2:
                return i
        return -1