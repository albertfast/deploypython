def encode_4_char_block(text):
    # Pad text to 4 characters if it has fewer characters
    text = text.ljust(4, '\0')  # Pad with null characters (ASCII 0)

    # Convert each character to its ASCII integer value
    ascii_values = [ord(char) for char in text]

    # Construct the 32-bit encoded value using the provided bit scrambling
    encoded_value = 0

    # Define the bit positions based on the challenge diagram
    bit_map = [
        (0, 0), (1, 0), (2, 0), (3, 0),
        (0, 1), (1, 1), (2, 1), (3, 1),
        (0, 2), (1, 2), (2, 2), (3, 2),
        (0, 3), (1, 3), (2, 3), (3, 3),
        (0, 4), (1, 4), (2, 4), (3, 4),
        (0, 5), (1, 5), (2, 5), (3, 5),
        (0, 6), (1, 6), (2, 6), (3, 6),
        (0, 7), (1, 7), (2, 7), (3, 7)
    ]

    # Loop through each bit map position and assign bits accordingly
    for bit_index, (char_index, char_bit_pos) in enumerate(bit_map):
        # Extract the bit from the ASCII character value
        bit_value = (ascii_values[char_index] >> char_bit_pos) & 1
        # Place the bit in the appropriate position in the encoded value
        encoded_value |= (bit_value << bit_index)

    return encoded_value


# Get input from the user
user_input = input("Enter a string (up to 4 characters): ")

# Encode the user input
encoded_value = encode_4_char_block(user_input)

# Print the encoded value
print(f"Encoded value for '{user_input}': {encoded_value}")
