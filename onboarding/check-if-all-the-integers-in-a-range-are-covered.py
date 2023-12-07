class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        contained=set()
        for val in ranges:
            for num in range(val[0],val[1]+1):
                if left<= num<=right:
                    contained.add(num)
      
        return len(contained)== right-left+1