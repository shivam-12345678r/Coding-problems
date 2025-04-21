class Solution:
    from collections import Counter
    from collections import defaultdict
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_ac = defaultdict(set)
        for id,time in logs:
            user_ac[id].add(time)
        print(user_ac)
        uam_cnt = Counter(len(time) for time in user_ac.values())
        print(uam_cnt)
        ans = [0]* k
        for uam,cnt in uam_cnt.items():
            if uam <= k:
                ans[uam - 1] = cnt
        return ans



        