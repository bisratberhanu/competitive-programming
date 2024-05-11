# Problem: IPO - https://leetcode.com/problems/ipo/

import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        arr = sorted(zip(capital, profits))
        maxheap = []
        i = 0

        while k > 0:
            while i < len(arr) and w >= arr[i][0]:
                heapq.heappush(maxheap, -arr[i][1])
                i += 1
            if not maxheap:
                break
            w -= heapq.heappop(maxheap)
            k -= 1

        return w