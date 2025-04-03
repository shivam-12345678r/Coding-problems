class Solution(object):
    def maxNumberOfBalloons(self, text):
        dict = {}
        for char in text:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
        bal_cnt = float('inf')
        for char in "balon":
            req = 2 if char in 'lo' else 1
            bal_cnt = min(bal_cnt,dict.get(char,0)//req)
        return bal_cnt

      
        