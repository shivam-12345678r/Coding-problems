class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def back(curr,open,close):
            if len(curr) == 2* n:
                res.append(curr)
                return
            if open < n:


                back(curr + '(', open + 1,close)
            if close < open:
                back(curr + ')', open, close + 1)
        back("",0,0)
        return res

        