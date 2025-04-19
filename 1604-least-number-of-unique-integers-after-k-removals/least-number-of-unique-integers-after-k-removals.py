import heapq
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        heap = []
        for value in freq.values():
            heapq.heappush(heap,value)
        while k > 0 and heap:
            k = k - heapq.heappop(heap)
        if k < 0 :
            return len(heap) + 1
        return len(heap)

