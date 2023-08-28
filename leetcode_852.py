class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
         
        for i in range(len(arr)-1):
            if i!=0 and arr[i+1]<arr[i]:
                return i

