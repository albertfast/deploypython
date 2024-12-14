# ================================UMPIRE========================================
# Understand:
# Given five input numbers, a, b, c, d and n, print out the number of 1 bits
# at the nth least significant bit position in all four numbers a, b, c, d.
# Example:  Input: 8 9 10 11 3 Output: 4

# Take input from the user
n1 = input("Enter four integers followed by the nth position (e.g., '2 3 5 6 1'): ")
lst_user_input = n1.split()

# Parse the input values
a = int(lst_user_input[0])
b = int(lst_user_input[1])
c = int(lst_user_input[2])
d = int(lst_user_input[3])
n = int(lst_user_input[4])

# Initialize the sum of LSBs
sum_of_lsbs = 0

# Step 2: Remove the nth bit from each value and extract the LSB
numbers = [a, b, c, d]
for number in numbers:
    # Right-shift the number by n to bring the nth bit to the LSB position
    nth_bit = (number >> n) & 1  # Isolate the nth bit
    sum_of_lsbs += nth_bit      # Add the nth bit to the sum

# Step 5: Print the sum
print("Sum of nth bits at position", n, ":", sum_of_lsbs)


# Second Way
def count_nth_bits(input_string):

    # Step 1: Parse the input
    inputs = list(map(int, input_string.split()))  # Convert all inputs to integers
    a, b, c, d, n = inputs  # Unpack the four numbers and the bit position

    # Step 2: Extract nth bits and count 1s
    numbers = [a, b, c, d]
    count_of_ones = 0

    for number in numbers:
        # Extract the nth bit
        nth_bit = (number >> n) & 1
        # Add to the count if nth bit is 1
        count_of_ones += nth_bit

    # Step 3: Return the total count of 1s
    return count_of_ones


# Example Usage
input_data = input("Enter four numbers and the nth position (e.g., '2 3 5 6 1'): ")
result = count_nth_bits(input_data)
print("Total count of '1's at nth bit position:", result)
