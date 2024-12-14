# Understand the Problem
# Problem Statement:
# - The input is a single line of text containing words.
# - For each word, count how many times it has occurred before in the input.
# - Output these counts in the same order as the words appear in the input.

# Inputs:
# - A single line of text containing words separated by spaces.

# Outputs:
# - A sequence of integers where each integer corresponds to the count of previous occurrences
#   of the respective word in the input text.

# Match the Problem to the Inputs/Outputs
# Inputs:
# - A string of words.
# Outputs:
# - A list of integers indicating the number of previous occurrences for each word.

# Plan the Solution
# Key Steps:
# 1. Parse the input text and split it into a list of words.
# 2. Use a dictionary to keep track of word occurrences.
# 3. Iterate through the list of words and for each word:
#    - Check the dictionary for how many times it has occurred before.
#    - Append this count to the output list.
#    - Update the dictionary to increment the count for this word.
# 4. Print the resulting list of counts as a space-separated string.

# Implement the Plan
def count_word_occurrences():
    # Step 1: Parse input text
    words = input().strip().split()  # Split input into a list of words

    # Step 2: Initialize a dictionary to track word occurrences
    word_count = {}
    result = []  # List to store the count of previous occurrences

    # Step 3: Iterate through the list of words
    for word in words:
        # Get the current count of the word from the dictionary, defaulting to 0
        count = word_count.get(word, 0)
        result.append(count)  # Append the count to the result list
        word_count[word] = count + 1  # Increment the word count in the dictionary

    # Step 4: Output the result as space-separated integers
    print(" ".join(map(str, result)))

# End the Program
count_word_occurrences()