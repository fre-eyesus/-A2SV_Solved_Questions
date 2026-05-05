# from heapq import heapify,heappop, heappush -> for heapfiy-min
from heapq import heapify_max,heappop_max, heappush_max
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heapify_max(piles)

        for i in range(k):
            temp = heappop_max(piles)

            temp = ceil(temp / 2)

            heappush_max(piles, temp)
        
        return sum(piles)

        