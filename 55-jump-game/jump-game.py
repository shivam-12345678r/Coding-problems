class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxin = 0
        for i in range(n):
            if i > maxin:
                return False
            maxin = max(maxin,i + nums[i])
        return True
        