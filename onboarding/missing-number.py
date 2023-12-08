class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,len(nums)):
            try:
                if nums[i]+1!=nums[i+1]:
                    return nums[i]+1
            except:
                if len(nums)!=1:
                    if nums[0]==0:
                        return nums[-1]+1
                    else:
                        return 0
                else:
                    if nums[0]==0:
                        return 1
                    else:
                        
                        return 0