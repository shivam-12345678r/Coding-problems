class Solution:
    def date_to_day(self, date: str) -> int:

         
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month, day = map(int, date.split('-'))
    
    # Sum up all full previous months and add current day
        return sum(days_in_month[:month - 1]) + day

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        ast = self.date_to_day(arriveAlice)
        ae = self.date_to_day(leaveAlice)
        ab = self.date_to_day(arriveBob)
        al = self.date_to_day(leaveBob)
        start = max(ast , ab)
        end = min(ae , al)
        if start <= end:
            return end - start + 1
        return 0

       

        