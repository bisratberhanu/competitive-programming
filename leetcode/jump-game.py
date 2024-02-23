class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True 
        maxval= nums[0]
        if maxval==0:
            return False 
        for i in range(len(nums)-1):
            maxval= max(maxval-1,nums[i+1])
            if maxval==0 and i!= len(nums)-2:
                return False
        return True