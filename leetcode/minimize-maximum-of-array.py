class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        """ a greedy approach
        the  minimum maximum cant be lower than the first value
        """

        maxval=  nums[0]
        total= nums[0]
        for i in range(1, len(nums)):
            total+= nums[i]
            median=  ceil(total/(i+1))
            maxval= max(maxval, median)
        return maxval