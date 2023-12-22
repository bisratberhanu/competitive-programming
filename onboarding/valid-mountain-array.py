class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3: return False
        maxval= max(arr)
        maxval_index= arr.index(maxval)
        if maxval_index==0 or maxval_index== len(arr)-1:
            return False
        for i in range(1, maxval_index+1):
            if arr[i]<=arr[i-1]:
                return False
        for i in range(maxval_index, len(arr)-1):
            if arr[i]<= arr[i+1]:
                return False
        return True