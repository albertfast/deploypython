import re

# Define the four strings to be tested.
string1 = "A man a plan a canal panama"
string2 = "ALPHA BRAVO CHARLIE DELTA ECHO FOXTROT"
string3 = "alphabravocharliedeltaechofoxtrot"
string4 = "0123456789"

# Create the regular expressions to be used.
# [a-z]+ matches one or more lowercase letters.
lowercase_pattern = re.compile(r"[a-z]+")
# [A-Z]+ matches one or more uppercase letters.
uppercase_pattern = re.compile(r"[A-Z]+")
# [0-9]+ matches one or more digits (0 to 9).
digit_pattern = re.compile(r"[0-9]+")

# Create a list of strings and their respective names for looping through.
strings = [
  (string1, "string1"),
  (string2, "string2"),
  (string3, "string3"),
  (string4, "string4"),
]

# Create a list of patterns and their respective descriptions for looping through.
patterns = [
    (lowercase_pattern, "lowercase letters"),
    (uppercase_pattern, "uppercase letters"),
    (digit_pattern, "digits"),
]

# Loop through each string.
for current_string, string_name in strings:
    # Loop through each pattern.
    for pattern, pattern_description in patterns:
        # Attempt to find a match.
        match = pattern.search(current_string)

        # Check if a match was found and output it to the console.
        if match:
            print(f"{string_name} matches a regular expression that indicates it has {pattern_description}")
        else:
            print(f"{string_name} does not match a regular expression that indicates it has {pattern_description}")