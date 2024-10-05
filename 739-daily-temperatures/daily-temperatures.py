class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [0] * n
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                ind = stack.pop()
                res[ind] = i - ind
            stack.append(i)
        return res


       
        