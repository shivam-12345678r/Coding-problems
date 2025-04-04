class Solution(object):
    def backspaceCompare(self, s, t):


        s1 = []
        s2 = []
        for num in s:

            if num != '#':
                s1.append(num)
            else:
                if s1:


                    s1.pop()
        for num in t:


            if num != '#':
                s2.append(num)
            else:
                if s2:
                    s2.pop()
        print(s1)
        print(s2)
        return s1 == s2
            