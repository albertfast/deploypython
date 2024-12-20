# ================================UMPIRE========================================
# Understand:
# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
#
# For example:
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28

def excel_column_to_number(column):
    """
    Convert a column title as appears in an Excel sheet to its corresponding column number.
    Assumption: Only up to 2-letter column titles are allowed.

    Args:
    column (str): Column title (e.g., "A", "Z", "AA", "ZY")

    Returns:
    tuple: Corresponding column number and the detailed computation steps as a string.
    """
    column = column.upper()  # Convert input to uppercase
    length_of_column = len(column)

    if length_of_column > 2:
        raise ValueError("Only up to 2-letter columns are allowed.")

    answer = 0
    detailed_steps = []

    for index, char in enumerate(column):
        n = ord(char) - ord('A') + 1
        if index == 0:
            detailed_steps.append(f"'{char}' is at the first position: value is {n}")
        else:
            detailed_steps.append(f"'{char}' is at position {index + 1}: value is {n}")
            detailed_steps.append(f"Applying formula: ({answer} * 26) + {n} = {answer * 26 + n}")
        answer = answer * 26 + n

    final_step = f"The final column number for '{column}' is {answer}"
    detailed_steps.append(final_step)

    computation_steps = "\n".join(detailed_steps)
    return answer, computation_steps


def main():
    column = input("Enter column title (up to 2 letters): ").strip()  # Strip any leading/trailing whitespace
    result, computation_steps = excel_column_to_number(column)
    print(f"Computation steps:\n{computation_steps}")


if __name__ == "__main__":
    main()



# def excel_column_to_number(column):
#     """
#     Convert a column title as appears in an Excel sheet to its corresponding column number.
#     Assumption: Only up to 2-letter column titles are allowed.
#
#     Args:
#     column (str): Column title (e.g., "A", "Z", "AA", "ZY")
#
#     Returns:
#     tuple: Corresponding column number and the computation steps as a string.
#     """
#     length_of_column = len(column)
#
#     if length_of_column > 2:
#         raise ValueError("Only up to 2-letter columns are allowed.")
#
#     answer = 0
#     steps = []
#
#     for i in range(length_of_column):
#         n = ord(column[i]) - ord('A') + 1
#         steps.append(f"({answer} * 26) + {n}")
#         answer = answer * 26 + n
#
#     computation_steps = " -> ".join(steps)
#     return answer, computation_steps
#
#
# def main():
#     column = input("Enter column title (up to 2 letters): ")
#     result, computation_steps = excel_column_to_number(column)
#     print(f"Computation steps: {computation_steps}")
#     print(f"The column number for '{column}' is: {result}")
#
#
#
# if __name__ == "__main__":
#     main()



# Example usage
# print(excel_column_to_number("ZY"))  # Output: 701
# print(excel_column_to_number("A"))  # Output: 1
# print(excel_column_to_number("AA"))  # Output: 27
# print(excel_column_to_number("AB"))  # Output: 28

'''
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        # Iterate through each character in the columnTitle string
        for i in range(len(columnTitle)):
            # Convert the character to its corresponding number (A = 1, B = 2, ..., Z = 26)
            # To achieve this, we use ord(char) to get the ASCII value of the character
            # Subtract ord('A') - 1 to normalize the value (so 'A' becomes 1 instead of its ASCII value)
            value = ord(columnTitle[i]) - ord("A") + 1

            # Multiply the current result by 26 (as each position represents a power of 26)
            # and add the current character's value
            result = result * 26 + value

        # Return the final result, which is the corresponding column number
        return result


# Example usage
solution = Solution()
'''
'''
def letter_to_number(c):
    # Convert a letter to a number where A=1, B=2, ..., Z=26
    num = ord(c) - 64
    return num

def title_to_number(columnTitle: str) -> int:
    result = 0
    # Iterate through each character in the columnTitle string
    for i in range(len(columnTitle)):
        # Convert the character to its corresponding number using letter_to_number function
        value = letter_to_number(columnTitle[i])

        # Multiply the current result by 26 and add the value of the current letter
        result = result * 26 + value

    # Return the final result, which is the corresponding column number
    return result

# Example usage
column = "AB"
print(title_to_number(column))  # Output will be 28
'''
'''
def excel_column_to_number(column):
    #1. Calculate length of input
    lengthOfColumn = len(column)

    #1.5 Initialize answer = 0
    answer = 0

    #2. Take one letter at a time in reverse order
    for i in range(lengthOfColumn):
        #3. For each of the letter LetterToNumber() -> n
        n = ord(column[lengthOfColumn - i - 1]) - 64

        #4. Calculate answer = answer + n * 26 raised to i
        # i = {0, 1, 2, 3 ...}
        answer += n * (26 ** i)

    #5. return answer
    return answer

'''
'''
def excel_column_to_number(column):
    #1. Calculate length of input
    lengthOfColumn = len(column)

    #1.5 Initialize answer = 0
    answer = 0
    i = 0;

    #2. Take one letter at a time in reverse order
    for index in range(lengthOfColumn -1, -1, -1):
        #3. For each of the letter LetterToNumber() -> n
        n = ord(column[index]) - 64;

        #4. Calculate answer = answer + n * 26 raised to i
        # i = {0, 1, 2, 3 ...}
        answer = answer+ n * (26 ** i);
        i = i + 1;

    #5. return answer
    return answer

'''
