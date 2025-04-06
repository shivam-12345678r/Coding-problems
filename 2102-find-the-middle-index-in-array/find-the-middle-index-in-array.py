class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        lsum = 0
        rsum = 0
        n = len(nums)
        total = sum(nums)
        if lsum == total - nums[0]:
            return 0
        for i in range(1,n):
            
           
            lsum +=  nums[i - 1]
            rsum = total - lsum - nums[i]
            if lsum == rsum:
                return i
        return -1

        