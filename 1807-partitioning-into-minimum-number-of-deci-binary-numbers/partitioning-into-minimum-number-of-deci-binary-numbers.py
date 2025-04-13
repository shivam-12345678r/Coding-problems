class Solution:
    def minPartitions(self, s: str) -> int:
        max_digit = None  # Initialize max_digit to None
        for char in s:
            if char.isdigit():  # Check if the character is a digit
                digit = int(char)  # Convert the character to an integer
                if max_digit is None or digit > max_digit:
                    max_digit = digit  # Update max_digit if a larger digit is found
        return max_digit

            