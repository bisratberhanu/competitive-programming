# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones= [-i for i in stones]
        heapify(stones)
        while len(stones)> 1:
            first= heappop(stones)
            second= heappop(stones)
            insertd= first- second
            if insertd:
                heappush(stones, insertd)
        if stones:
            return stones[0]* -1
        return 0

