class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        l,r = 0,n - 1
        while l <= r:
            m = (l + r)//2
            if m > 0 and nums[m] < nums[m - 1]:

                r  = m - 1
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1
            else:
                return m
    
        """
        :type nums: List[int]
        :rtype: int
        """
        