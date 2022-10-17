class Solution:
    from typing import List 
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer=[]
        for val in nums1:
            x= nums2.index(val)
            for val2 in nums2[x:]:
                if val2>val:
                    answer.append(val2)
                    break
                elif val2==nums2[-1]: 
                    answer.append(-1)
                    
        return answer