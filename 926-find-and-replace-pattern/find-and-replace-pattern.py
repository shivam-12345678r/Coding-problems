class Solution:
    def get_p(self,word):
        char_map = {}
        pattern = []
        for char in word:
            if char not in char_map:
                char_map[char] = len(char_map)
            pattern.append(char_map[char])
        return pattern





    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern_c = self.get_p(pattern)
        match = [word for word in words if self.get_p(word) == pattern_c]
        return match
        