class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cnt = 0
        costs.sort()
        for num in costs:
            if coins - num >= 0:
                coins = coins - num
                cnt += 1
        return cnt