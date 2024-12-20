import re

class RegexExamples:
    """
    A class to demonstrate the usage of Python Regular Expressions with examples.
    """

    def __init__(self, pattern):
        """
        Initializes the RegexExamples class with a given pattern.

        :param pattern: A string representing the regex pattern.
        """
        self.pattern = re.compile(pattern)  # Compile the regex pattern for efficiency

    def match_example(self, text):
        """
        Matches the pattern at the beginning of the text.

        :param text: The input string to match against the pattern.
        :return: The match groups if a match is found, otherwise a message.
        """
        match = self.pattern.match(text)
        if match:
            return match.groups()  # Returns all groups in the match as a tuple
        else:
            return "No match found at the beginning of the text."

    def search_example(self, text):
        """
        Searches for the pattern anywhere in the text.

        :param text: The input string to search against the pattern.
        :return: The match groups if a match is found, otherwise a message.
        """
        search = self.pattern.search(text)
        if search:
            return search.groups()  # Returns all groups in the search as a tuple
        else:
            return "No match found in the text."

    def findall_example(self, text):
        """
        Finds all non-overlapping matches of the pattern in the text.

        :param text: The input string to search.
        :return: A list of all matches.
        """
        return self.pattern.findall(text)  # Returns a list of all matches

    def replace_example(self, text, replacement):
        """
        Replaces all occurrences of the pattern in the text with the replacement.

        :param text: The input string where the pattern should be replaced.
        :param replacement: The string to replace the matched pattern with.
        :return: The modified string.
        """
        return self.pattern.sub(replacement, text)  # Replace matches with replacement

# Additional Examples

def example_email_extraction():
    """
    Extracts email addresses from a given string.
    """
    text = "ali@example.com veli.45@test.net ayşe_123@mail.org"
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    result = re.findall(pattern, text)
    return result  # Output: ['ali@example.com', 'veli.45@test.net', 'ayşe_123@mail.org']

def example_date_replacement():
    """
    Replaces hyphens with slashes in a date string.
    """
    text = "Date: 2023-10-26"
    pattern = r'-'
    new_text = re.sub(pattern, '/', text)
    return new_text  # Output: Date: 2023/10/26

def example_word_boundary():
    """
    Matches whole word "cat" using word boundaries.
    """
    text = "cat cats category"
    pattern_boundary = r"\bcat\b"
    pattern_no_boundary = r"cat"
    boundary_result = re.findall(pattern_boundary, text)
    no_boundary_result = re.findall(pattern_no_boundary, text)
    return boundary_result, no_boundary_result  # Output: (['cat'], ['cat', 'cat', 'cat'])

# Main function for testing

def main():
    print("Character class example (Find all vowels):")
    vowel_example = RegexExamples(r"[aeiou]")
    print(vowel_example.findall_example("mother of all battles"))  # Output: ['o', 'e', 'o', 'a', 'a', 'e']

    print("\nGrouping example:")
    group_example = RegexExamples(r"(\d+)\.(\d+)")
    print(group_example.match_example("27.1835"))  # Output: ('27', '1835')

    print("\nOptional group example:")
    optional_example = RegexExamples(r"(\d+)\.?(\d+)?")
    print(optional_example.match_example("27"))  # Output: ('27', None)
    print(optional_example.match_example("27.0"))  # Output: ('27', '0')

    print("\nGreedy vs Non-Greedy example:")
    greedy_example = RegexExamples(r"<.*>")  # Greedy match
    print(greedy_example.findall_example("<html><body></body></html>"))  # Output: ['<html><body></body></html>']

    non_greedy_example = RegexExamples(r"<.*?>")  # Non-greedy match
    print(non_greedy_example.findall_example("<html><body></body></html>"))  # Output: ['<html>', '<body>', '</body>', '</html>']

    print("\nReplace example:")
    replace_example = RegexExamples(r"\d+")
    print(replace_example.replace_example("The price is 100 dollars", "XXX"))  # Output: "The price is XXX dollars"

    print("\nEmail Extraction:")
    print(example_email_extraction())  # Output: ['ali@example.com', 'veli.45@test.net', 'ayşe_123@mail.org']

    print("\nDate Replacement:")
    print(example_date_replacement())  # Output: Date: 2023/10/26

    print("\nWord Boundary Example:")
    boundary_result, no_boundary_result = example_word_boundary()
    print("With word boundary:", boundary_result)  # Output: ['cat']
    print("Without word boundary:", no_boundary_result)  # Output: ['cat', 'cat', 'cat']

if __name__ == "__main__":
    main()
