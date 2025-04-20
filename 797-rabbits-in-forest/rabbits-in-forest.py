class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        seen = Counter(answers)
        total = 0
        for ans,value in seen.items():
            groups = (ans + value) // (ans + 1)
            total += groups *(ans + 1)

        return total
        