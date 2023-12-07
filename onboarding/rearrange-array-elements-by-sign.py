class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[0 for i in range(len(nums))]
        ptr1,ptr2=0,1
        for i in range(len(nums)):
            if nums[i]>0:
                ans[ptr1]= nums[i]
                ptr1+=2
            else:
                ans[ptr2]= nums[i]
                ptr2+=2
        return ans 
        