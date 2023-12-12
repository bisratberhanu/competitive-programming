class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans=0
        for left in range(len(nums)-2):
            a= nums[left]
            b= nums[left+1]
            c= nums[left+2]
            if a < b + c:
                return a+b+c
        return ans 
        
        
         
         
