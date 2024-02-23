class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        minval= float(inf)
        for i in range(len(nums)):

            while stack and nums[i]>= stack[-1][0]:
                stack.pop()
            if stack and stack[-1][1]< nums[i]:
                return True 
            minval= min(minval, nums[i])
            stack.append([nums[i], minval])

        return False 
        