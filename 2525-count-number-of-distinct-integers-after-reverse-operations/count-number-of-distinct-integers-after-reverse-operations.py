class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinct = set()
        for num in nums:
            distinct.add(num)
            rev = int(str(num)[::-1])
            distinct.add(rev)
        return len(distinct)
        