# Importing the Solution class
from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # Dictionary to map words to their indices for quick lookup
        word_map = {word: i for i, word in enumerate(words)}
        result = []

        # Function to check if a string is a palindrome
        def is_palindrome(word):
            return word == word[::-1]

        # Iterate through all words and their indices
        for idx, word in enumerate(words):
            n = len(word)
            # Split the word into all possible prefix and suffix substrings
            for j in range(n + 1):
                prefix = word[:j]  # Prefix substring
                suffix = word[j:]  # Suffix substring

                # Case 1: If prefix is a palindrome, check if the reverse of the suffix exists
                if is_palindrome(prefix):
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix in word_map and word_map[reversed_suffix] != idx:
                        result.append([word_map[reversed_suffix], idx])

                # Case 2: If suffix is a palindrome and j != n to avoid duplicates
                if j != n and is_palindrome(suffix):
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in word_map and word_map[reversed_prefix] != idx:
                        result.append([idx, word_map[reversed_prefix]])

        return result


# Test cases for PyCharm
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    words1 = ["abcd", "dcba", "lls", "s", "sssll"]
    print("Input:", words1)
    print("Output:", solution.palindromePairs(words1))
    print("Expected: [[0, 1], [1, 0], [3, 2], [2, 4]]\n")

    # Test Case 2
    words2 = ["bat", "tab", "cat"]
    print("Input:", words2)
    print("Output:", solution.palindromePairs(words2))
    print("Expected: [[0, 1], [1, 0]]\n")

    # Test Case 3
    words3 = ["a", ""]
    print("Input:", words3)
    print("Output:", solution.palindromePairs(words3))
    print("Expected: [[0, 1], [1, 0]]\n")

    # Test Case 4 - Edge Case with single letter words
    words4 = ["a", "b", "c", "aa", "bb", "cc"]
    print("Input:", words4)
    print("Output:", solution.palindromePairs(words4))
    print("Expected: []\n")

    # Test Case 5 - Large Input Example
    words5 = ["race", "car", "ecarace", "rac", "e"]
    print("Input:", words5)
    print("Output:", solution.palindromePairs(words5))
    print("Expected: [[0, 1], [1, 0], [3, 0], [0, 4]]\n")
