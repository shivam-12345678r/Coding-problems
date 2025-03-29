class Solution(object):
    def countBits(self, n):
        res = []
        for i in range(n + 1):
            k = bin(i).count('1')
            res.append(k)
        return res


        """
        :type n: int
        :rtype: List[int]
        """
        