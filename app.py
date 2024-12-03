from flask import Flask, request, render_template
from bitMap1 import encode_text  # Adjust based on the actual function name in bitMap1.py

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get user input from the form
        user_input = request.form.get('user_input')

        # Ensure the input is valid and call the encode function from bitMap1.py
        if user_input:
            encoded_value = encode_text(user_input)  # Use the function from bitMap1.py
            return render_template('index.html', result=f'Encoded Value: {", ".join(map(str, encoded_value))}')
        else:
            return render_template('index.html', result='Please provide valid input.')

    # Render the initial form
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
