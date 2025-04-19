from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = Counter(nums)
        domin = 0
        for num,cnt in freq.items():
            if cnt > len(nums) // 2:
                domin = num
        lc = 0
        tc = freq[domin]
        for i in range(len(nums)):
            if nums[i] == domin:
                lc += 1
            if lc > (i + 1)//2 and (tc - lc) > (len(nums) - i - 1)//2:
                return i
        return -1
                
        