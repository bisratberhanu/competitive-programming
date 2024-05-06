# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # find the common prefix
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift