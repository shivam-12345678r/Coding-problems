class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        cur,res = set(),set()
        for num in arr:
            cur = {num | x for x in cur} | {num}
            res |= cur
        return len(res)
