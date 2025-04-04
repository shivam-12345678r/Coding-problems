class Solution(object):
    def minBitFlips(self, start, goal):
        ans = start ^ goal
        cnt = 0
        while ans:
            cnt += ans & 1
            ans >>= 1
        return cnt
     

        
   
        