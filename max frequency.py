 def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        lo, hi = 0, 1
        while hi < len(nums):
            k -= (nums[hi] - nums[hi - 1]) * (hi - lo)
            if k < 0:
                k += nums[hi] - nums[lo]
                lo += 1
            hi += 1
        return hi - lo