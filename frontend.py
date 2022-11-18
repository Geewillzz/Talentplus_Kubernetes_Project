from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/frontend', methods=['GET', 'POST'])
def home():
    response = requests.get('http://127.0.0.1:5001/backend')
    displayed_text = response.content
    print (displayed_text)
    #displayed_text = requests.get("http://127.0.0.1:5001").json().
    return displayed_text

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)