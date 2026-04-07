class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        lo = 0
        hi = x
        ans = 0
        while lo <= hi:
            mid = (hi + lo)//2
            if mid <= x/mid:
                ans = mid 
                lo = mid + 1
            else:
                hi = mid - 1
        return ans

        """
        :type x: int
        :rtype: int
        """
        