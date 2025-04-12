class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        map = {}
        res = []
        for i in range(len(A)):
            map[A[i]] = map.get(A[i],0) + 1
            map[B[i]] = map.get(B[i],0) + 1

            cnt = 0
            for key,value in map.items():
                if value == 2:
                    cnt += 1
            res.append(cnt)
        return res


        