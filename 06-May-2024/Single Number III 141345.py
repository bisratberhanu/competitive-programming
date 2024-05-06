# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_two_nums = 0
        for num in nums:
            xor_two_nums ^= num

        set_bit = xor_two_nums & -xor_two_nums # gives a result only the first different bit is 1

        num1 = num2 = 0
        for num in nums:
            if num & set_bit:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]