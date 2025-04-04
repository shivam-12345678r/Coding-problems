class Solution(object):
    def hammingDistance(self, x, y):
        ans = x ^ y
        flips = 0
        while ans:
            flips += ans & 1
            ans = ans >> 1
        return flips
        
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        