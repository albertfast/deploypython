import unittest

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers: left starts at the beginning, right starts at the end
        left, right = 0, len(s) - 1

        # Iterate while the left pointer is less than the right pointer
        while left < right:
            # If the character at 'left' is not alphanumeric, move the left pointer forward
            if not s[left].isalnum():
                left += 1
                continue

            # If the character at 'right' is not alphanumeric, move the right pointer backward
            if not s[right].isalnum():
                right -= 1
                continue

            # Compare characters at left and right pointers (case insensitive)
            # Use .lower() to convert both characters to lowercase
            if s[left].lower() != s[right].lower():
                return False  # Return False if characters do not match

            # Move both pointers towards the center
            left += 1
            right -= 1

        # If all characters match, return True (the string is a palindrome)
        return True


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_palindrome(self):
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(self.solution.isPalindrome("racecar"))
        self.assertTrue(self.solution.isPalindrome("No lemon, no melon"))
        self.assertTrue(self.solution.isPalindrome(""))

    def test_invalid_palindrome(self):
        self.assertFalse(self.solution.isPalindrome("race a car"))
        self.assertFalse(self.solution.isPalindrome("hello world"))
        self.assertFalse(self.solution.isPalindrome("palindrome"))

    def test_edge_cases(self):
        self.assertTrue(self.solution.isPalindrome(" "))
        self.assertTrue(self.solution.isPalindrome("a"))
        self.assertTrue(self.solution.isPalindrome("aa"))
        self.assertFalse(self.solution.isPalindrome("ab"))

if __name__ == '__main__':
    unittest.main()
