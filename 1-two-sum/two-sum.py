class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {}
        n = len (nums)
        for i in range(n):
            comp = target - nums[i]
            if comp in nummap:
                return [nummap[comp],i]
            nummap[nums[i]] = i
        return []
        