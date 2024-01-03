class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        r=1
        while r<len(nums):
            if nums[l]==nums[r]:
                nums[r]=1000
                r+=1
            else:
                l=r
                r+=1
        nums.sort()
        k=0
        for i in nums:
            if i!=1000:
                k+=1
            else: break
        nums= nums[0:k]
        return k
