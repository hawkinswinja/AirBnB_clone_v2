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


@app.route('/c/<text>')
def display_c(text):
    """display web"""
    if '_' in text:
        text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python')
@app.route('/python/<text>')
def display_python(text='is cool'):
    """display web"""
    if '_' in text:
        text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def display_int(n):
    """display only if number"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
