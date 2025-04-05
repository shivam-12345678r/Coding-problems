class Solution(object):
   

    def totalHammingDistance(self, nums):
        flips = 0
        n = len(nums)
        for bit in range(32):
            count_1 = 0
            for num in nums:
                if (num >> bit) & 1:
                    count_1 += 1
            count_0 = n - count_1
            flips += count_1 * count_0
      
        return flips

        