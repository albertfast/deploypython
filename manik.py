def reverse_bit_manipulation(binary_string):
  """
  Reverses the bit manipulation based on a pre-defined reverse bit map.

  Args:
    binary_string: The binary string to be reversed (32 bits long).

  Returns:
    The reversed binary string.
  """

  if len(binary_string) != 32:
    raise ValueError("Binary string must be exactly 32 bits long.")

  reverse_bit_map = [
      0, 1, 2, 3,  # Original 0-3 bit positions
      4, 5, 6, 7,  # Original 4-7 bit positions
      8, 9, 10, 11, # Original 8-11 bit positions
      12, 13, 14, 15, # Original 12-15 bit positions
      16, 17, 18, 19, # Original 16-19 bit positions
      20, 21, 22, 23, # Original 20-23 bit positions
      24, 25, 26, 27, # Original 24-27 bit positions
      28, 29, 30, 31  # Original 28-31 bit positions
  ]

  reversed_bits = [None] * 32
  for i in range(len(reverse_bit_map)):
    reversed_bits[reverse_bit_map[i]] = binary_string[i]

  return ''.join(reversed_bits)

def apply_bit_manipulation(binary_string):
  """
  Applies bit manipulation based on a pre-defined bit map.

  Args:
    binary_string: The binary string to be manipulated (32 bits long).

  Returns:
    The manipulated binary string.
  """

  if len(binary_string) != 32:
    raise ValueError("Binary string must be exactly 32 bits long.")

  bit_map = [
      24, 16, 8, 0,  # 0-3 bits
      25, 17, 9, 1,  # 4-7 bits
      26, 18, 10, 2, # 8-11 bits
      27, 19, 11, 3, # 12-15 bits
      28, 20, 12, 4, # 16-19 bits
      29, 21, 13, 5, # 20-23 bits
      30, 22, 14, 6, # 24-27 bits
      31, 23, 15, 7  # 28-31 bits
  ]

  manipulated_bits = [None] * 32
  for i in range(len(bit_map)):
    manipulated_bits[i] = binary_string[bit_map[i]]

  return ''.join(manipulated_bits)

def encode_text(text):
  """
  Encodes a text string using the bit manipulation algorithm.

  Args:
    text: The text string to be encoded.

  Returns:
    A tuple containing the encoded binary string, encoded decimal value, and decoded raw binary string.
  """

  if len(text) * 8 != 32:
    raise ValueError("Input text must be 4 characters long (32 bits total).")

  binary_string = ''.join([format(ord(char), '08b') for char in text])

  # Get Decoded/Raw format first (reversed binary)
  decoded_raw = reverse_bit_manipulation(binary_string)
  print(f"Decoded/Raw: {decoded_raw}")

  # Encode using the Decoded/Raw format
  encoded_binary = apply_bit_manipulation(decoded_raw)
  encoded_value = int(encoded_binary, 2)

  print(f"Encoded Binary: {encoded_binary}")
  print(f"Encoded Value (Decimal): {encoded_value}")

  return encoded_binary, encoded_value, decoded_raw

def main():
    text = input("Lütfen şifrelenecek metni giriniz: ")
    encoded_binary, encoded_value, decoded_raw = encode_text(text)
    print("Encoded Binary:", encoded_binary)
    print("Encoded Value (Decimal):", encoded_value)
    print("Decoded/Raw:", decoded_raw)

if __name__ == "__main__":
    main()
