class Solution(object):
    def minStartValue(self, nums):
        start = 0
        curr_sum = start
        min_sum = float('inf')
        n = len(nums)
        for i in range(n):
            curr_sum += nums[i]
            min_sum = min(min_sum,curr_sum)
        start = 1 - (min_sum)
        if min_sum > 0:
            return 1
        return start


       