class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right= max(weights), sum(weights) 
        ans=left
        def checker(n):
            summ=0
            cur_days=1
            for val in weights:
                summ+= val
                if summ> n:
                    cur_days+=1
                    summ= val
                if cur_days > days:
                    return False
            return True  
                 


       
        
        
        while left<= right:
            mid= (left+right)//2
            if checker(mid):
                right= mid-1
                ans=mid
            else:
                left= mid+1
        
        return ans
