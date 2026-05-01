class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def back(start,curr):
            if len(curr) == k:
                res.append(curr[:])
                return
            needed = k - len(curr)
            avl = n - start + 1
            if avl < needed:
                return 
            
            for i in range(start, n + 1):
                curr.append(i)
                back(i + 1,curr)
                curr.pop()
        back(1,[])
        return res


        