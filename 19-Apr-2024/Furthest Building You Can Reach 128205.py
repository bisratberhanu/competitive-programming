# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap= []
        cur_bricks=0
        for i in range(len(heights)-1):
            if heights[i] >= heights[i+1]:
                continue
            diff= heights[i+1]- heights[i]
            
            print(len(heap))
            if len(heap) < ladders:
                heappush(heap, diff)
                
            else:
                
                if heap and heap[0] < diff:
                    
                    min_element= heappop(heap)
                    heappush(heap, diff)
                    cur_bricks+= min_element
                else:
                    cur_bricks+= diff
                if cur_bricks > bricks:
                    return i
        return len(heights)-1
            


