from flask import Flask, request, render_template
from bitMap1 import encode_4_char_block  # encode_4_char_block fonksiyonunuz varsa

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['user_input']
        encoded_value = encode_4_char_block(user_input)  # encode fonksiyonunuzu burada kullanın
        return render_template('index.html', result=encoded_value)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
