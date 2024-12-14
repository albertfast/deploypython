import re

# Define the strings to test
string1 = "A man a plan a canal panama"
string2 = "ALPHA BRAVO CHARLIE DELTA ECHO FOXTROT"
string3 = "alphabravocharliedeltaechofoxtrot"
string4 = "0123456789"

# Define the regular expressions
regex_lowercase = r"[a-z]+"  # Matches one or more lowercase letters
regex_uppercase = r"[A-Z]+"  # Matches one or more uppercase letters
regex_digits = r"\d+"        # Matches one or more digits

# Function to test a string against a pattern
def test_string(string, regex, description):
    """Checks if the string matches the given regex and returns a descriptive message."""
    if re.search(regex, string):  # If the string matches the pattern
        return f"matches a regular expression that indicates it has {description}."
    else:  # If the string does not match the pattern
        return f"does not match a regular expression that indicates it has {description}."

# Main program logic
def main():
    """
    This program tests 4 predefined strings against 3 regular expressions.
    For each string, it determines whether it matches patterns for:
    - lowercase letters
    - uppercase letters
    - digits
    """
    # Predefined strings
    strings = [
        ("string1", string1),
        ("string2", string2),
        ("string3", string3),
        ("string4", string4),
    ]

    # Regular expressions and their descriptions
    regexes = [
        (regex_lowercase, "lowercase letters"),
        (regex_uppercase, "uppercase letters"),
        (regex_digits, "digits"),
    ]

    # Test each string with each regex
    for string_name, string in strings:
        print(f"\nTesting {string_name}: \"{string}\"")
        for regex, description in regexes:
            result = test_string(string, regex, description)
            print(f"{string_name} {result}")

# Run the program
if __name__ == "__main__":
    main()
