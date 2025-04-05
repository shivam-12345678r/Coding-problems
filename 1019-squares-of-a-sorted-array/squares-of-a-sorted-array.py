class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        l = 0
        r = n - 1
        res = [0] * n
        index = n - 1
        while l <= r:
            if abs(nums[r]) > abs(nums[l]):
                res[index] = nums[r]**2
                r -= 1
            else:
 
                res[index] = nums[l]**2
                l += 1
            index -= 1
        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        