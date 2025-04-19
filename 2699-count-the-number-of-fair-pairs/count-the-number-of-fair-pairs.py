class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        
        n = len(nums)
        
       
        def cnt_less(x):
            low = 0
            right = n - 1
            cnt = 0


            while low <= right:
                if nums[low] + nums[right] <= x:
                    cnt += (right - low)
                    low += 1
                else:
                    right -= 1
            return cnt
        count = cnt_less(upper) - cnt_less(lower - 1)
        return count