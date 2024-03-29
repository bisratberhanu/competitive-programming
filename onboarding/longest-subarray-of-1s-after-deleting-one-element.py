class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxlength=0
        count=0
        left=0
        for right in range(len(nums)):
            if nums[right]==0:
                count+=1
            while count>1:
                if nums[left]==0: count-=1
                left+=1
            maxlength= max(maxlength, right-left)
        return maxlength