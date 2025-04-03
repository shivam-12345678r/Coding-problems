class Solution(object):
    def lemonadeChange(self, bills):
        five,ten = 0 , 0
        n = len(bills)
        for i in range(n):
            if bills[i] == 5:
                five += 1
            elif  bills[i] == 10 and five:
                ten += 1
                five -= 1
            else:
                if ten > 0 and five > 0:

                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True

        
        