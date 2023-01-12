#!/usr/bin/python3
"""module containing function hello_world"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """function to return the default page of web server"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """display hbnb"""
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
