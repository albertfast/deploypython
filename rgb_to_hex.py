# n the previous problem, one of the issues you may have run into was an empty substring.
# In Python, "" in any string will always be True, despite the problem requiring False.
# This exception brings up the following question: Is it better to handle this input in the function,
# or stop the function and tell users to abide by the function's requirements?
# Pre-conditions are requirements that must be True for a given piece of code to work.
# For example, a pre-condition in the last problem is that the range numbers (a & b) can't be negative numbers.
# Although negative numbers may work in the slice operator, it won't work in the function,
# nor are there any safeguards to prevent negative numbers from being used in the function. You can specify pre-conditions in a comment:
# def matching_substring(s, sub, a, b):
     # Pre-cond: a >= 0, b >= 0
# When writing tests, it's important to think about what pre-conditions to consider.
# If you know certain situations won't appear because it's defined as a precondition,
# you can safely ignore them, as long as it's mentioned in the function's description.
# Additionally, we could also choose to handle select pre-conditions, returning a special output (like False or an empty string).
# We'll practice handling pre-conditions in the next problem.

# Problem Statement:
# Given a 3-number RGB color code, convert it into a hexadecimal color code:
# Ex: (17, 10, 255) => "110aff" (17 => "11", 10 => "0a", 255 => "ff")
# Numbers are 3 integers between 0 and 255 (inclusive). You should check if numbers fall into this range (pre-condition)
# If this pre-condition fails, return an empty string
# Hexadecimal color codes are always 6-letters
# Example:              Input:                  Output:
#           	     145, 0, 255                "9100ff"
#                    0, 0, 0                    "000000"
#                   -1, 0, 0                    ""

def rgb_to_hex(r, g, b):
    '''Convert rbg color code to hex string. If rgb color is invalid, returns empty string'''
    # Pre-condition: r, g, b must be between 0 and 255
    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        return f"{r:02x}{g:02x}{b:02x}"  # Convert to hex
    else:
        return ""  # Invalid RGB value returns empty string

# Test Cases
if __name__ == "__main__":
    try:
        r, g, b = map(int, input("Enter 3 numbers, separated by space (r g b): ").split())
        result = rgb_to_hex(r, g, b)
        if result:
            print(f"rgb_to_hex({r}, {g}, {b}) = {result}")
        else:
            print("Invalid RGB values. Please enter values between 0 and 255.")
    except ValueError:
        print("Invalid input. Please enter 3 valid numbers separated by space.")


    test_cases = [
        (145, 0, 255),  # Expected: "9100ff"
        (0, 0, 0),  # Expected: "000000"
        (255, 255, 255),  # Expected: "ffffff"
        (-1, 0, 0),  # Expected: ""
        (300, 0, 0),  # Expected: ""
        (128, -20, 255),  # Expected: ""
        (12, 200, 50)  # Expected: "0cc832"
    ]

    for r, g, b in test_cases:
        result = rgb_to_hex(r, g, b)
        print(f"rgb_to_hex({r}, {g}, {b}) = {result}")


