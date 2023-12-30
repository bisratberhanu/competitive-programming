class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        sorted_lis= sorted(nums)
        for val in nums:
            temp= bisect_left(sorted_lis,val)
            ans.append(temp)
        return ans 