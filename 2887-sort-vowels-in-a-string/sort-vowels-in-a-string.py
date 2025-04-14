class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        vowel_indices = []
        for i, char in enumerate(s):
            if char.lower() in 'aeiou':
                vowels.append(char)
                vowel_indices.append(i)

        vowels.sort()  # Sort the vowels list

        result_list = list(s) #convert string to list so that we can change the characters

        for i, vowel in zip(vowel_indices, vowels):
            result_list[i] = vowel #replace the original vowels with sorted vowels

        return "".join(result_list)
        