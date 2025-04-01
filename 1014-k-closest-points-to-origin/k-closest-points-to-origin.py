import heapq
import math
class Solution(object):


    def kClosest(self,points, k):
        heap = []  # Max heap to store (distance, point) pairs

        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            if len(heap) < k:
                heapq.heappush(heap, (-distance, [x, y]))  # Negate distance for max heap
            else:
                if distance < -heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-distance, [x, y]))

        result = [point for _, point in heap]
        return result

        