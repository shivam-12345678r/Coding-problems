class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        size = 0

        cnt = [0] * 31
        for num in candidates:
            for i in range(31):
                if num & (1 << i):
                    cnt[i] += 1
        return max(cnt)
