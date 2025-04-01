import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        n = len(stones)
        if n == 1:
            return stones[0]
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones)> 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones,-(y - x))
        return -stones[0] if stones else 0

        
        
        
       
        