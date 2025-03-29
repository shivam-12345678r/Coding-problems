class Solution(object):
    def hammingWeight(self, n):
        cnt = 0
        while n:
            if n & 1 == 1:
                cnt += 1
            n = n//2
        return cnt
        """
        :type n: int
        :rtype: int
        """
        