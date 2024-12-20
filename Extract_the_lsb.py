# Binary representation of 5
num = 5  # Binary: 101

# Using LSB 0 numbering
print("Bit 2 (LSB 0):", (num >> 2) & 1)  # Output: 1 (most significant bit)

# Using LSB 1 numbering
print("Bit 2 (LSB 1):", (num >> 1) & 1)  # Output: 0 (middle bit)

# Removing n bits
n = 2
removed = num >> n
print("Number after removing 2 bits:", removed)  # Output: 1 (Binary: 1)

# Extracting the LSB
lsb = num & 1
print("Least Significant Bit (LSB):", lsb)  # Output: 1


# def extract_lsb(number):
#     """
#     Extract the Least Significant Bit (LSB) of an integer.
#
#     Args:
#         number (int): The integer whose LSB is to be extracted.
#
#     Returns:
#         int: The LSB (either 0 or 1).
#     """
#     # Perform bitwise AND operation to isolate the LSB
#     lsb = number & 1  # The result will be 1 if LSB is set, otherwise 0
#
#     # Print detailed steps for better understanding
#     print(f"Binary representation of {number}: {bin(number)[2:]}")
#     print(f"Performing {number} & 1 gives {lsb} (The LSB)")
#
#     return lsb
#
#
# # Example Usage:
# number = 29  # Binary: 11101
# result = extract_lsb(number)
# print(f"The Least Significant Bit (LSB) of {number} is: {result}")

