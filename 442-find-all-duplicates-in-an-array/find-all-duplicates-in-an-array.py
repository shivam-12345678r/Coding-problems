class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                dup.append(abs(num))
            else:
                nums[index] = -nums[index]
        return dup
        