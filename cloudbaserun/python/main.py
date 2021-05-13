import os

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return request.remote_addr + ";" + request.environ['REMOTE_ADDR'] + ";" + request.environ['HTTP_X_FORWARDED_FOR']
    #return 'Hello World!'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
