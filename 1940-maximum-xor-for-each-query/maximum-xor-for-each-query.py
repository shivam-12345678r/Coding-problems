class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xorr = 0
        for num in nums:
            xorr = xorr ^ num
        max_k = (1 << maximumBit) - 1
        res = []
        for i in range(len(nums)):
            res.append(xorr ^ max_k)
            xorr ^= nums[-1]
            nums.pop()
        return res

        