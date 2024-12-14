# Understand:
    # The goal is to find the word with the highest frequency in a given string.
    # If there is a tie (multiple words with the same frequency), the lexicographically smallest word is returned.
    # The input string may include punctuation, uppercase letters, and repetitive words.

    # Match:
    # This is a frequency problem, so we need to:
    # - Use a dictionary to count the occurrences of each word.
    # - Preprocess the string to handle punctuation and convert everything to lowercase.
    # - Use sorting to handle ties and find the correct word.
    # Tools: Dictionary for frequency counting, sorting for ties.

    # Plan:
    # 1. Preprocess the string: Remove punctuation and convert to lowercase.
    # 2. Use a dictionary to count the frequency of each word.
    # 3. Sort the dictionary:
    #    - By frequency in descending order.
    #    - Lexicographically for words with the same frequency.
    # 4. Return the most frequent word.

    # Preprocess:
def highestFrequency(str):
    # Step 1: Preprocess the string to remove punctuation
    str = str.lower().replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace("(", "").replace(")", "").replace("'", "")

    # Step 2: Initialize a dictionary to count the frequency of each word
    frequency = {}

    # Step 3: Split the string into words
    words = str.split()

    # Step 4: Count the frequency of each word
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    # Step 5: Find the word with the highest frequency
    # Sort the dictionary by frequency (descending) and lexicographical order for ties
    most_frequent = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))[0][0]

    return most_frequent

# Evaluate:
# - Ensure punctuation is correctly removed.
# - Ensure ties are resolved lexicographically.
# - Test with multiple cases to confirm functionality.