def encode_text(text):
  binary_string = ''.join(format(ord(char), '08b') for char in text)
  print(f"Binary String: {binary_string}")

  decodedRaw = reverse_bit_manipulation(binary_string)
  print(f"Decoded/Raw: {decodedRaw}")  # Bu satırı tekrar ekledik

  encoded_binary = apply_bit_manipulation(decodedRaw)
  encoded_value = int(encoded_binary, 2)

  print(f"Encoded Value (Decimal): {encoded_value}")
  print(f"Encoded Binary: {encoded_binary}")

  return encoded_value, encoded_binary

def decode_text(encoded_binary):
    decoded_binary = reverse_bit_manipulation(encoded_binary)
    
    text = ''.join(chr(int(decoded_binary[i:i+8], 2)) for i in range(0, len(decoded_binary), 8))
    
    print(f"Decoded Text: {text}")
    
    return text


def apply_bit_manipulation(binary_string):
    if len(binary_string) != 32:
        raise ValueError("Binary string must be exactly 32 bits long.")
    
    manipulated_bits = [''] * 32
    
    bit_map = [
        24, 16, 8, 0,    # 0-3 bits
        25, 17, 9, 1,    # 4-7 bits
        26, 18, 10, 2,   # 8-11 bits
        27, 19, 11, 3,   # 12-15 bits
        28, 20, 12, 4,   # 16-19 bits
        29, 21, 13, 5,   # 20-23 bits
        30, 22, 14, 6,   # 24-27 bits
        31, 23, 15, 7    # 28-31 bits
    ]
    
    for i, bit_index in enumerate(bit_map):
        manipulated_bits[i] = binary_string[bit_index]
    
    return ''.join(manipulated_bits)

def reverse_bit_manipulation(encoded_binary):
    if len(encoded_binary) != 32:
        raise ValueError("Binary string must be exactly 32 bits long.")
    
    reversed_bits = [''] * 32
    
    reverse_bit_map = [
        3, 11, 19, 27,   # 0-3 bits (reverse order)
        2, 10, 18, 26,   # 4-7 bits
        1, 9, 17, 25,    # 8-11 bits
        0, 8, 16, 24,    # 12-15 bits
        7, 15, 23, 31,   # 16-19 bits
        6, 14, 22, 30,   # 20-23 bits
        5, 13, 21, 29,   # 24-27 bits
        4, 12, 20, 28    # 28-31 bits
    ]
    
    for i, bit_index in enumerate(reverse_bit_map):
        reversed_bits[bit_index] = encoded_binary[i]
    
    return ''.join(reversed_bits)


# Örnek kullanım:
input_text = "^^^^"
encoded_value, encoded_binary = encode_text(input_text)

# Encode sonucu tekrar decode edelim
decoded_text = decode_text(encoded_binary)
