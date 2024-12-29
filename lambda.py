def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

bit_map = [0, 8, 16, 24, 1, 9, 17, 25, 2, 10, 18, 26, 3, 11, 19, 27, 4, 12, 20, 28, 5, 13, 21, 29, 6, 14, 22, 30, 7, 15, 23, 31]

def apply_bit_manipulation(binary_str):
    return ''.join(binary_str[i] if i < len(binary_str) else '0' for i in bit_map)

def reverse_bit_manipulation(enc_binary):
    decoded_binary = ['0'] * 32  # Ensure the array is filled with default '0'
    for i, pos in enumerate(bit_map):
        if i < len(enc_binary):
            decoded_binary[pos] = enc_binary[i]
    return ''.join(decoded_binary)

def encode_text(input_text):
    input_blocks = [input_text[i:i+4] for i in range(0, len(input_text), 4)]
    encoded_values = []
    for block in input_blocks:
        binary_str = text_to_binary(block).ljust(32, '0')  # Padding to 32 bits
        manipulated_binary = apply_bit_manipulation([binary_str[i:i+8] for i in range(0, len(binary_str), 8)][::-1])
        encoded_values.append(int(manipulated_binary, 2))
    return encoded_values

def decode_text(encoded_values):
    decoded_text = ''
    for value in encoded_values:
        bin_str = format(value, '032b')
        decoded_raw = reverse_bit_manipulation([bin_str[i:i+8] for i in range(0, len(bin_str), 8)][::-1])
        decoded_text += binary_to_text(decoded_raw)
    return decoded_text.replace('\x00', '')  # Remove padding

# Test input and process
input_text = "Test"
encoded_values = encode_text(input_text)
decoded_text = decode_text(encoded_values)

print("Original Text:", input_text)
print("Encoded Values:", encoded_values)
print("Decoded Text:", decoded_text)
