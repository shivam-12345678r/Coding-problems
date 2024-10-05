class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        max_alt = 0
        for chng in gain:
            alt += chng
            max_alt = max(max_alt,alt)
        return max_alt
        