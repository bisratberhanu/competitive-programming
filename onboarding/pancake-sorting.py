class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        counter= len(arr)
        ans=[]
        for i in range(len(arr)):
            maxidx= arr.index(max(arr[0:counter]))
            arr= arr[:maxidx+1][::-1]+arr[maxidx+1:]
            ans.append(maxidx+1)
            arr=arr[:counter][::-1]+ arr[counter:]
            ans.append(counter)
            counter-=1
        return ans 
        
