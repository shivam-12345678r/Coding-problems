class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def backtrack(index,distribution):
            if index == len(cookies):
                return max(distribution)
            min_unfair = float('inf')
            for i in range(k):
                distribution[i] += cookies[index]
                min_unfair = min(min_unfair,backtrack(index + 1,distribution))
                distribution[i] -= cookies[index]
                if distribution[i] == 0:
                    break
            return min_unfair
        distribution = [0] * k
        return backtrack(0,distribution)

