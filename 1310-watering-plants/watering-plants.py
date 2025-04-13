class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cnt = 1
        n = len(plants)
        left = capacity - plants[0]
        for i in range(1,n):
            if left >= plants[i]:
                cnt += 1
                left -= plants[i]
            else:
                cnt += 2*(i + 1) - 1
                left = capacity - plants[i]
        return cnt


        