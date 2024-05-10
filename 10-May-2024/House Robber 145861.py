# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            if i < 0:
                return 0
            case1= dp(i-2)
            case2= dp(i-1)
            if case1 + nums[i] > case2:
                return case1 + nums[i]
            else:
                return case2
        
        return dp(len(nums)-1)
            