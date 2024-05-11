# Problem: Target Sum - https://leetcode.com/problems/target-sum/

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(i, cursum):
            if (i, cursum) in memo:
                return memo[(i, cursum)]
            if i == len(nums):
                return 1 if cursum == target else 0

            memo[(i, cursum)] = dp(i + 1, cursum + nums[i]) + dp(i + 1, cursum - nums[i])
            return memo[(i, cursum)]

        return dp(0, 0)