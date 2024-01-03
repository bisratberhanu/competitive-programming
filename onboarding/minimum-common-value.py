class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.append(float('inf'))
        nums2.append(float('inf'))
        ptr1,ptr2=0,0
        while ptr1< len(nums1):
            if ptr1==len(nums1)-1 and ptr2==len(nums2)-1:
                return -1
            if nums1[ptr1]==nums2[ptr2]:
                return nums1[ptr1]
            if nums1[ptr1]<nums2[ptr2]:
                ptr1+=1
            else:
                ptr2+=1
        