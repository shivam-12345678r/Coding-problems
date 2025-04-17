class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        cnt = 1
        nums.sort()
        min_val = nums[0]
        for i in range(1,len(nums)):
            if nums[i] - min_val > k:
                cnt += 1
                min_val = nums[i]
        return cnt 
        