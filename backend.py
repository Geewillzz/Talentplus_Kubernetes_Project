import jsonify
from flask import Flask

app = Flask(__name__)

@app.route('/backend', methods=['GET', 'POST'])
def get_text():
    key_word = "TALENT PLUS"
    return key_word
   # return jsonify(key_word=key_word)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5001)