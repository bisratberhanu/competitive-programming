class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # for each two values in sorted iterate through  the third, 
        # every subarray to the left is also c 
        nums.sort(reverse= True)
        n= len(nums)
        if n<= 2:
            return 0
        
        ans=0
        for first in range(n-2):
            second= first+1
            third= n-1
            while second< third:
                if nums[second] + nums[third]> nums[first]:
                    ans+= third- second
                    second+=1

                else:
                    third-=1

        return ans 
                


