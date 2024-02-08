class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr= [0]*1001
        for num,start,end in trips:
            arr[start]+= num
            arr[end]-= num
        acc=0
        for i in range(len(arr)):
            acc+= arr[i]
            arr[i]= acc
        return max(arr)<= capacity