class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi = 0
        curr = 0
        for i in range(k):
            maxi += nums[i]
        curr = maxi
        for i in range(k,len(nums)):
            curr += nums[i] - nums[i - k]
            maxi = max(maxi,curr)
        return maxi/k
        