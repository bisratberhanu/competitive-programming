class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        def helper(mid):
            arr= []
            for val in heaters:
                temp=[]
                left= val- mid
                right= val + mid 
                temp.append(left)
                temp.append(right)
                arr.append(temp)
            ptr,i =0,0
            while i< len(arr) and ptr< len(houses):
                if arr[i][0]<= houses[ptr] <= arr[i][1]:
                    ptr+=1
                else:
                    i+=1
            if ptr< len(houses):
                return False
            return True  



        left,right= 0, 10**9

        while left<= right:
            mid= (left+right)//2
            if helper(mid):
                right= mid-1
            else:
                left= mid+1
        return left 