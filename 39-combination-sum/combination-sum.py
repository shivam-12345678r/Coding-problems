class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for can in candidates:
            for i in range(can,target + 1):
                for comb in dp[i - can]:
                    dp[i].append(comb + [can])
        return dp[target]

        