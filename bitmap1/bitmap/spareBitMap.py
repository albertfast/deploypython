from flask import Flask, request, render_template
import re

app = Flask(__name__)

# Define the bitMap and scrambleMap
#bit_map = [0, 8, 16, 24, 1, 9, 17, 25, 2, 10, 18, 26, 3, 11, 19, 27, 4, 12, 20, 28, 5, 13, 21, 29, 6, 14, 22, 30, 7, 15, 23, 31]
bit_map = [i + 8 * j for i in range(8) for j in range(4)]
original = 'XWVUTSRQ PNMLKJHG FEDCBA98 76543210'
scrambled = 'XPF7WNE6 VMD5ULC4 TKB3SJA2 RH91QG80'
scramble_map = dict(zip(original, scrambled))
reverse_scramble_map = {v: k for k, v in scramble_map.items()}

print('Bit Map:', bit_map)
print('Scramble Map:', scramble_map)
print('Reverse Scramble Map:', reverse_scramble_map)


# Function to apply bit manipulation
def apply_bit_manipulation(binary):
    result = ''.join(binary[bit_map[i]] for i in range(32))
    print('Apply Bit Manipulation Result:', result)
    return result


# Function to reverse bit manipulation
def reverse_bit_manipulation(binary):
    decoded_binary = [''] * 32
    for i in range(32):
        decoded_binary[bit_map[i]] = binary[i]
    result = ''.join(decoded_binary)
    print('Reverse Bit Manipulation Result:', result)
    return result


# Helper functions to convert text to binary and vice versa
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)


def binary_to_text(binary):
    return ''.join(chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8))


# Encode text
def encode_text(input_text):
    encoded_values = []
    print('Input Text:', input_text)
    # Split the input text into 4-char blocks (if less than 4 chars, pad with spaces)
    for block in re.findall('.{1,4}', input_text):
        print('Current 4-char block:', block)
        binary = text_to_binary(block).ljust(32, '0')
        reversed_blocks = ''.join([binary[i:i + 8] for i in range(24, -1, -8)])
        print('Binary (reversed blocks):', reversed_blocks)
        manipulated_binary = apply_bit_manipulation(reversed_blocks)
        print('Manipulated Binary:', manipulated_binary)
        decimal_value = int(manipulated_binary, 2)
        encoded_values.append(decimal_value)
    print('Encoded Values:', encoded_values)
    return encoded_values


# Decode text
def decode_text(encoded_values):
    decoded_text = ''
    print('Encoded Values for Decoding:', encoded_values)
    for value in encoded_values:
        binary = format(value, '032b')
        print('Binary from Decimal Value:', binary)
        reversed_binary = reverse_bit_manipulation(binary)
        print('Reversed Binary:', reversed_binary)
        reversed_blocks = ''.join([reversed_binary[i:i + 8] for i in range(24, -1, -8)])  # Corrected sequence
        print('Decoded Raw Binary (reversed again):', reversed_blocks)
        decoded_text += binary_to_text(reversed_blocks).replace('\x00', '')
    print('Decoded Text:', decoded_text)
    return decoded_text


# Scramble and descramble functions
def scramble_text(input_text):
    scrambled_result = ''.join(scramble_map.get(char, char) for char in input_text)
    print('Scrambled Text:', scrambled_result)
    return scrambled_result


def descramble_text(scrambled_text):
    descrambled_result = ''.join(reverse_scramble_map.get(char, char) for char in scrambled_text)
    print('Descrambled Text:', descrambled_result)
    return descrambled_result


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    scrambled_result = None
    descrambled_result = None
    decoded_text = None

    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if 'encode' in request.form:
            result = encode_text(user_input)
        elif 'scramble' in request.form:
            scrambled_result = scramble_text(user_input)
        elif 'descramble' in request.form:
            descrambled_result = descramble_text(user_input)
        elif 'decode' in request.form:
            encoded_values = [int(x) for x in user_input.split(',')]
            decoded_text = decode_text(encoded_values)

    return render_template('index.html', result=result, scrambled_result=scrambled_result,
                           descrambled_result=descrambled_result, decoded_text=decoded_text)


if __name__ == '__main__':
    app.run(debug=True)
