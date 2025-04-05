class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = 0
        n = len(cost)
        if n <= 2:
            return min(cost[0],cost[1])
        dp1 = cost[0]
        dp2 = cost[1]
        for i in range(2,n):
            curr = cost[i] + min(dp1,dp2)
            dp1 = dp2
            dp2 = curr
        return min(dp1,dp2)
        