class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        seen=set()
        for val in nums1:
            if val in nums2 and val not in seen:
                temp1= nums1.count(val)
                temp2= nums2.count(val)
                seen.add(val)
                for i in range(min(temp1,temp2)):
                    ans.append(val)
        return ans 

