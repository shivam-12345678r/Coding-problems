from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        frq = Counter(s)
        len = 0
        odd = False
        for cnt in frq.values():
            len += cnt//2 * 2
            if cnt % 2 == 1:
                odd = True
        if odd:
            len += 1
        return len





      
        