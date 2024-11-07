from flask import Flask, request, jsonify
from bitMap1 import encode_4_char_block  # Import the encoding function from your script

app = Flask(__name__)

@app.route('/encode', methods=['POST'])
def encode_text():
    data = request.get_json()
    text = data.get("text", "")
    encoded_value = encode_4_char_block(text)
    return jsonify({"encoded_value": encoded_value})

if __name__ == '__main__':
    app.run(debug=True)
