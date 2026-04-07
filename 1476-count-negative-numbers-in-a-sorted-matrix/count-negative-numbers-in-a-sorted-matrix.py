class Solution(object):
    def countNegatives(self, grid):
        if not grid:
            return 0
        m,n = len(grid),len(grid[0])
        total = 0
        for row in grid:
            lo = 0
            hi = n
            while lo < hi:
                mid = (lo + hi)//2
                if row[mid] >= 0:
                    lo = mid + 1
                else:
                    hi = mid 
            total += n - lo
        return total






        """
        :type grid: List[List[int]]
        :rtype: int
        """
        