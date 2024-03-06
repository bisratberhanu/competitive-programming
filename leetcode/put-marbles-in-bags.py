class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        if k== len(weights):# each belong to one bag
            return 0
        arr= []
        maxval= minval= 0
        for i in range(len(weights)-1):
            arr.append(weights[i]+ weights[i+1])
        arr.sort()

        # for min val and maxval
        for i in range(k-1):
            minval+= arr[i]
            maxval+= arr[len(arr)-1-i]
        return maxval-minval

            
