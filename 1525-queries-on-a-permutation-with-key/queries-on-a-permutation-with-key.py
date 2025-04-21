class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        perm = [0] * m
        for i in range(m):
            perm[i] = i + 1
        res = []
        for query in queries:
            pos = perm.index(query)
            res.append(pos)
            perm.insert(0,perm.pop(pos))
        return res

        