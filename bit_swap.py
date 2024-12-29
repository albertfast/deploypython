def encode_text(text):
  binary_string = ''.join(format(ord(char), '08b') for char in text)
  print(f"Binary String: {binary_string}")

  encoded_binary = apply_bit_manipulation(binary_string)
  encoded_value = int(encoded_binary, 2)

  print(f"Encoded Value (Decimal): {encoded_value}")
  print(f"Encoded Binary: {encoded_binary}")

  return encoded_value, encoded_binary

def apply_bit_manipulation(binary_string):
    # Burada binary stringi manipüle edelim
    manipulated_bits = ''
    
    # Örneğin, blokları tersine çevirmek için:
    for i in range(len(binary_string), 0, -8):
        block = binary_string[i-8:i]
        print(f"Original Block: {block}")
        manipulated_bits += block  # Blokları olduğu gibi ekle veya burada bir manipülasyon uygula
        print(f"Manipulated Bits: {manipulated_bits}")
    
    return manipulated_bits

def reverse_bit_manipulation(encoded_binary):
    # Burada manipülasyonu tersine çevirelim
    reversed_bits = ''
    
    for i in range(len(encoded_binary), 0, -8):
        block = encoded_binary[i-8:i]
        reversed_bits = block + reversed_bits  # Blokları tersine çevirme işlemi
        print(f"Reversed Block: {block}")
    
    return reversed_bits


def decode_text(encoded_binary):
    decoded_binary = reverse_bit_manipulation(encoded_binary)
    
    text = ''.join(chr(int(decoded_binary[i:i+8], 2)) for i in range(0, len(decoded_binary), 8))
    
    print(f"Decoded Text: {text}")
    
    return text

# Örnek kullanım:
input_text = "a@b."
encoded_value, encoded_binary = encode_text(input_text)

# Encode sonucu tekrar decode edelim
decoded_text = decode_text(encoded_binary)
