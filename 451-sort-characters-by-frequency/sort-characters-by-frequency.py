from collections import Counter
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        freq_map = Counter(s)
        max_heap = [(-freq,char) for char,freq in freq_map.items()]
        heapq.heapify(max_heap)
        res = []
        while max_heap:
            freq,char = heapq.heappop(max_heap)
            res.append(char * -freq)
        return ''.join(res)



        