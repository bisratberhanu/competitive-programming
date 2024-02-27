class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm=[]
        def backTrack(perm_each):
            if len(perm_each)== len(nums):
                perm.append(perm_each[:])
                return
             
            
            for val in nums:
                if val not in perm_each:
                    perm_each.append(val)
                    backTrack(perm_each)
                    perm_each.pop()
        
        backTrack([])
        return perm 
