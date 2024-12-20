def text_to_binary(text):
    # Converts text to binary, with each character as 8-bit binary
    return ''.join(format(ord(char), '08b') for char in text)


def binary_to_text(binary):
    # Converts binary back to text by interpreting each 8-bit chunk as a character
    return ''.join(chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8))


# The bit manipulation map to rearrange bits
bit_map = [
    0, 8, 16, 24, 1, 9, 17, 25,
    2, 10, 18, 26, 3, 11, 19, 27,
    4, 12, 20, 28, 5, 13, 21, 29,
    6, 14, 22, 30, 7, 15, 23, 31
]


def apply_bit_manipulation(binary_str):
    # Reorder the bits in `binary_str` according to `bit_map`
    return ''.join(binary_str[i] if i < len(binary_str) else '0' for i in bit_map)


def reverse_bit_manipulation(enc_binary):
    # Reverse the bit manipulation by applying `bit_map` in reverse
    decoded_binary = ['0'] * 32  # Initialize with 32 zeros
    for i, pos in enumerate(bit_map):
        if i < len(enc_binary):
            decoded_binary[pos] = enc_binary[i]
    return ''.join(decoded_binary)


def encode_text(input_text):
    # Split input text into chunks of 4 characters each
    input_blocks = [input_text[i:i + 4] for i in range(0, len(input_text), 4)]
    encoded_values = []
    for block in input_blocks:
        # Convert text block to binary and pad to 32 bits
        binary_str = text_to_binary(block).ljust(32, '0')
        # Manipulate bits and convert to integer
        manipulated_binary = apply_bit_manipulation([binary_str[i:i + 8] for i in range(0, len(binary_str), 8)][::-1])
        encoded_values.append(int(manipulated_binary, 2))
    return encoded_values


def decode_text(encoded_values):
    decoded_text = ''
    for value in encoded_values:
        # Convert integer back to 32-bit binary
        bin_str = format(value, '032b')
        # Reverse bit manipulation
        decoded_raw = reverse_bit_manipulation([bin_str[i:i + 8] for i in range(0, len(bin_str), 8)][::-1])
        # Convert binary back to text
        decoded_text += binary_to_text(decoded_raw)
    return decoded_text.replace('\x00', '')  # Remove padding


# Main program loop
while True:
    print("\nBit Manipulation Encoder/Decoder")
    print("1. Encode Text")
    print("2. Decode Text")
    print("3. Clear Screen")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        input_text = input("Enter text to encode: ")
        encoded_values = encode_text(input_text)
        print("\nResults:")
        print("Input Text:", input_text)
        print("Encoded Value (Decimal):", ", ".join(map(str, encoded_values)))

    elif choice == '2':
        input_decimal = input("Enter comma-separated encoded values: ")
        encoded_values = list(map(int, input_decimal.split(',')))
        decoded_text = decode_text(encoded_values)
        print("\nResults:")
        print("Encoded Value (Decimal):", input_decimal)
        print("Decoded Text:", decoded_text)

    elif choice == '3':
        print("\033c", end="")  # Clears the console screen

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please select a valid option.")
