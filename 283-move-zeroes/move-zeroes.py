class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        one = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero],nums[i] = nums[i],nums[zero]
                zero += 1
    





        """
        Do not return anything, modify nums in-place instead.
        """
        