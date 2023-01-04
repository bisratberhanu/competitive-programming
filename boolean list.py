from typing import List 
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        booleanlist=[]
        for i in range(len(l)):
            k= nums[l[i]:r[i]+1]
            
            k.sort()
            for i in range(len(k)-1):
                if k[i+1] - k[i] != k[1] - k[0]:
                    booleanlist.append(False)
                    break
            else:
                booleanlist.append(True) 
        return booleanlist