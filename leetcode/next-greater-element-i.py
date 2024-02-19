class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        dic= {}
        for val in nums2:
            while  stack and val > stack[-1]:
                dic[stack.pop()]= val
            
            
            stack.append(val)
        ans=[]
        for val in nums1:
            if val in dic:
                ans.append(dic[val])
            else:
                ans.append(-1)
        return ans  