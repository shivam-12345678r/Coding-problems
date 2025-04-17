class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_oc = {char:idx for idx,char in enumerate(s)}
        start,end = 0,0
        res = []
        for i ,char in enumerate(s):
            end = max(end,last_oc[char])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res
        