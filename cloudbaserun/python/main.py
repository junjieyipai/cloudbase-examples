import os

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'I want T-shirt'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
