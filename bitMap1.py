from flask import Flask, request, render_template, session, redirect, url_for
import re

app = Flask(__name__)
app.secret_key = 'Change'

# Define the bitMap and scrambleMap
bit_map = [i + 8 * j for i in range(8) for j in range(4)]
original = 'XWVUTSRQ PNMLKJHG FEDCBA98 76543210'
scrambled = 'XPF7WNE6 VMD5ULC4 TKB3SJA2 RH91QG80'
scramble_map = dict(zip(original, scrambled))
reverse_scramble_map = {v: k for k, v in scramble_map.items()}

# Function to apply bit manipulation
def apply_bit_manipulation(binary):
    result = ''.join(binary[bit_map[i]] for i in range(32))
    return result

# Function to reverse bit manipulation
def reverse_bit_manipulation(binary):
    decoded_binary = [''] * 32
    for i in range(32):
        decoded_binary[bit_map[i]] = binary[i]
    result = ''.join(decoded_binary)
    return result

# Helper functions to convert text to binary and vice versa
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    return ''.join(chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8))

# Encode text
def encode_text(input_text):
    encoded_values = []
    for block in re.findall('.{1,4}', input_text):
        binary = text_to_binary(block).ljust(32, '0')
        reversed_blocks = ''.join([binary[i:i + 8] for i in range(24, -1, -8)])
        manipulated_binary = apply_bit_manipulation(reversed_blocks)
        decimal_value = int(manipulated_binary, 2)
        encoded_values.append(decimal_value)
    return encoded_values

# Decode text
def decode_text(encoded_values):
    decoded_text = ''
    for value in encoded_values:
        binary = format(value, '032b')
        reversed_binary = reverse_bit_manipulation(binary)
        reversed_blocks = ''.join([reversed_binary[i:i + 8] for i in range(24, -1, -8)])
        decoded_text += binary_to_text(reversed_blocks).replace('\x00', '')
    return decoded_text

# Scramble and descramble functions
def scramble_text(input_text):
    scrambled_result = ''.join(scramble_map.get(char, char) for char in input_text)
    return scrambled_result

def descramble_text(scrambled_text):
    descrambled_result = ''.join(reverse_scramble_map.get(char, char) for char in scrambled_text)
    return descrambled_result

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'results' not in session:
        session['results'] = []

    if request.method == 'POST':
        if 'clear' in request.form:
            session['results'] = []
            return redirect(url_for('index'))

        input_text = request.form.get('input_text')
        input_decimal = request.form.get('input_decimal')

        if 'encode' in request.form and input_text:
            encoded_values = encode_text(input_text)
            session['results'].append(f'Encoded Value: {", ".join(map(str, encoded_values))}')
        elif 'scramble' in request.form and input_text:
            scrambled_result = scramble_text(input_text)
            session['results'].append(f'Scrambled Text: {scrambled_result}')
        elif 'descramble' in request.form and input_text:
            descrambled_result = descramble_text(input_text)
            session['results'].append(f'Descrambled Text: {descrambled_result}')
        elif 'decode' in request.form and input_decimal:
            encoded_values = [int(x) for x in input_decimal.split(',')]
            decoded_text = decode_text(encoded_values)
            session['results'].append(f'Decoded Text: {decoded_text}')

        session.modified = True
        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
