from typing import List
from functools import lru_cache

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(start, target, path):
            if target == 0:
                res.append(path[:])
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                dfs(i, target - candidates[i], path + [candidates[i]])

        dfs(0, target, [])
        return res
