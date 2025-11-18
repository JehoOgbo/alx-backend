#!/usr/bin/env python3
""" Basic flask app
"""
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def welcome() -> Response:
    return Response(render_template('0-index.html'))


if __name__ == '__main__':
    app.run(debug=True)
