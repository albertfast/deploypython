# Understand
# Given a number n, followed by n lines of text, print all words encountered in the text, one per line,
# with their number of occurrences in the text.
# The words should be sorted in descending order according to their number of occurrences,
# and all words within the same frequency should be printed in lexicographical order.
#
# Hint. After you created a dictionary of the words and their frequencies,
# you would like to sort it according to the frequencies.
# This can be achieved if you create a list whose elements are lists of two elements:
# the number of occurrences of a word and the word itself. For example, [[2, 'hi'], [1, 'what'], [3, 'is']].
# Then the standard list sort will sort a list of lists, with the lists compared by the first element, and if these are equal,
# by the second element. This is nearly what is required.

# Example:    Input:                                Output:
#             9                                     damme 4
#             hi                                    is 3
#             hi                                    name 3
#             what is your name                     van 3
#             my name is bond                       hi 2
#             james bond                            claude 2
#             my name is damme                      bond 2
#             van damme                             my 2
#             claude van damme                      james 1
#             jean claude van damme                 jean 1
#                                                   what 1
#                                                   your 1

def frequency_analysis():
    # Outer Loop (for _ in range(n)):
    # This loop runs n times, where n is the number of lines of text to process.
    # Each iteration reads one line of text.
    n = int(input().strip())  # Read number of lines and strip unnecessary spaces

    # Dictionary to store word frequencies
    frequency = {}

    # Inner Loop (for word in input().strip().split()):
    # input(): Reads the line of text.
    # .strip(): Removes leading and trailing spaces from the input.
    # .split(): Splits the line into individual words, using spaces as the delimiter.
    # Example:
    # Input: "my name is damme"
    # After split(): ["my", "name", "is", "damme"]
    # The loop iterates over each word in the line.
    for _ in range(n):
        for word in input().strip().split():
            # frequency[word] = frequency.get(word, 0) + 1:
            # frequency.get(word, 0):
            # - Checks if the word already exists in the dictionary frequency.
            # - If the word exists, it returns its current count.
            # - If the word doesn't exist, it returns 0 (default value).
            # + 1:
            # - Increments the word's count by 1.
            # frequency[word] = ...:
            # - Updates the dictionary with the new count for the word.
            # Example:
            # First encounter of "my":
            # - frequency.get("my", 0) returns 0.
            # - frequency["my"] = 0 + 1 sets the count to 1.
            # Second encounter of "my":
            # - frequency.get("my", 0) returns 1.
            # - frequency["my"] = 1 + 1 sets the count to 2.
            frequency[word] = frequency.get(word, 0) + 1

    # Sorting the words by their frequency (descending) and lexicographically for ties
    # sorted(frequency, key=lambda x: (-frequency[x], x)):
    # - Sorting by -frequency[x] ensures descending order of frequency.
    # - Sorting by x ensures lexicographical order in case of ties.
    sorted_words = sorted(frequency, key=lambda x: (-frequency[x], x))

    # Print each word with its frequency
    for word in sorted_words:
        print(word, frequency[word])

# Call the function to execute
frequency_analysis()






















