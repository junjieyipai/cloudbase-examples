import os

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    if 'HTTP_X_FORWARDED_FOR' in request.environ:
        return request.environ['HTTP_X_FORWARDED_FOR'].split(',')[0]
    return request.remote_addr

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
