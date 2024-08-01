# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True 
        maxv= nums[0]
        if maxv==0:
            return False 
        for i in range(len(nums)-1):
            maxv= max(maxv-1,nums[i+1])
            if maxv==0 and i!= len(nums)-2:
                return False
        return True