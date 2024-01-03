class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroptr=0 
        numptr=0
        while zeroptr<len(nums) and numptr<len(nums):
            while zeroptr<len(nums) and  nums[zeroptr]!=0 :
                zeroptr+=1
            numptr=zeroptr+1
            while numptr<len(nums) and nums[numptr]==0 :
                numptr+=1
            if  zeroptr==len(nums) or  numptr==len(nums):
                break
        
            nums[zeroptr],nums[numptr]= nums[numptr],nums[zeroptr]
            

        
         
        