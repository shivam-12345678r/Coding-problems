class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_coins = 0
        n = len(piles) // 3
        for i in range(n):
            max_coins += piles[-(2 * (i + 1))]
        return max_coins
