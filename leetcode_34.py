class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       # using the bisect library
       
       if not nums or target>nums[-1] or target< nums[0]:
           return [-1,-1]
       left= bisect_left(nums,target)
       right= bisect_right(nums,target)
       if left==right:
           return [-1,-1]
       else:
            return[left,right-1]
        
          
        
