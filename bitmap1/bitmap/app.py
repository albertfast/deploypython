from flask import Flask, request, render_template
from bitMap1 import encode_text  # Adjust based on the actual function name in bitMap1.py

app = Flask(__name__)

HOST = "0.0.0.0"
PORT = 5000


def process_input(input_text):
    """Handles encoding of the user input text."""
    if not input_text:
        return 'Please provide valid input.'
    encoded_value = encode_text(input_text)
    return f'Encoded Value: {", ".join(map(str, encoded_value))}'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_text = request.form.get('user_input')
        result = process_input(input_text)
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
