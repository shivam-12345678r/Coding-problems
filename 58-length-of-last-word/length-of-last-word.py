class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = ''
        n = len(s)
        for i in range(n - 1,-1,-1):
            if s[i].isalnum():
                c += s[i]
            elif len(c) and not s[i].isalnum():
                break
        return len(c)

        