class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backTrack(index, summ, lis):
            if summ> n or len(lis)> k:
                return 
            if summ== n and len(lis)==k:
                ans.append(lis[:])
                return 
            
            for i in range(index, 10):
                lis.append(i)
                backTrack(i+1, summ+i,lis)
                lis.pop()
            
        backTrack(1,0, [])
        return ans
                
        