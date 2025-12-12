"""
To run in terminal:
`FLASK_APP=py_scripts/basic_http_requests.py flask run`
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'