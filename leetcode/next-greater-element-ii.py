class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n= len(nums)
        ans= [-1]*n
        stack=[]
        maxelement= max(nums)

        for i in range(2*n):
            
            while stack and nums[stack[-1]] < nums[i%n]:
                popped= stack.pop()
                ans[popped%n]= nums[i%n]
            stack.append(i%n)
        return ans 