class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        end=len(arr)
        res=[]
        while end>1:
            maxInd=arr.index(end) 
            if maxInd==end-1: 
                end-=1
                continue

            #making the max element at Index 0, unless if it already was at index 0
            if maxInd!=0:
                arr[:maxInd+1]=reversed(arr[:maxInd+1])
                res.append(maxInd+1) 
                
                
            
            arr[:end]=reversed(arr[:end])
            res.append(end)
            
            end-=1
        return res    