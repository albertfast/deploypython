def text_to_binary(text):
    # Convert each character in the text to its 8-bit binary representation
    return ''.join(format(ord(char), '08b') for char in text)

def apply_bit_manipulation(binary_string):
    # Expecting a 32-bit binary string
    if len(binary_string) != 32:
        raise ValueError("Binary string must be exactly 32 bits long.")
    
    manipulated_bits = [''] * 32

    # Bit reordering map (according to the provided input)
    bit_map = [
        0, 8, 16, 24,    # Take the first byte to the beginning
        1, 9, 17, 25,    
        2, 10, 18, 26,   
        3, 11, 19, 27,   
        4, 12, 20, 28,   
        5, 13, 21, 29,   
        6, 14, 22, 30,   
        7, 15, 23, 31    
    ]

    # Rearrange the bits according to the bit map
    for i, bit_index in enumerate(bit_map):
        manipulated_bits[i] = binary_string[bit_index]

    return ''.join(manipulated_bits)

def reverse_bit_manipulation(encoded_binary):
    # Expecting a 32-bit binary string
    if len(encoded_binary) != 32:
        raise ValueError("Binary string must be exactly 32 bits long.")
    
    reversed_bits = [''] * 32

    # Bit reordering map (reversing the manipulation)
    bit_map = [
        0, 8, 16, 24,    # Take the first byte to the beginning
        1, 9, 17, 25,    
        2, 10, 18, 26,   
        3, 11, 19, 27,   
        4, 12, 20, 28,   
        5, 13, 21, 29,   
        6, 14, 22, 30,   
        7, 15, 23, 31    
    ]

    # Rearrange the bits back to their original positions
    for i, bit_index in enumerate(bit_map):
        reversed_bits[bit_index] = encoded_binary[i]

    return ''.join(reversed_bits)

def encode_text(text):
    binary_string = text_to_binary(text)
    
    # Ensure the binary string is 32 bits long (pad with zeros if necessary)
    binary_string = binary_string.ljust(32, '0')
    print(f"Binary String: {binary_string}")

    # Find the Decoded/Raw format by reversing the byte order
    decoded_raw = ''.join(binary_string[i:i+8] for i in range(24, -1, -8))
    print(f"Decoded/Raw: {decoded_raw}")

    # Perform bit manipulation on the Decoded/Raw binary string
    encoded_binary = apply_bit_manipulation(decoded_raw)
    encoded_value = int(encoded_binary, 2)

    print(f"Encoded Binary: {encoded_binary}")
    print(f"Encoded Value (Decimal): {encoded_value}")

    return binary_string, decoded_raw, encoded_binary, encoded_value

def decode_text(encoded_binary):
    # Reverse the bit manipulation
    decoded_binary = reverse_bit_manipulation(encoded_binary)
    
    # Reverse the byte order to get the original binary string
    decoded_raw = ''.join(decoded_binary[i:i+8] for i in range(24, -1, -8))
    
    # Convert the binary string back to text
    text = ''.join(chr(int(decoded_raw[i:i+8], 2)) for i in range(0, len(decoded_raw), 8))

    return text

# Get input from the user
input_text = input("Enter the text you want to encode: ")

# Perform the encoding process
binary_string, decoded_raw, encoded_binary, encoded_value = encode_text(input_text)

# Decode the encoded data back to text
decoded_text = decode_text(encoded_binary)
print(f"Decoded Text: {decoded_text}")
