#!/usr/bin/env python3
""" Basic flask app
"""
from flask import Flask, render_template, Response, request
from flask_babel import Babel # type: ignore



class Config:
    """ configure languages supported by your app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def welcome() -> Response:
    return Response(render_template('2-index.html'), mimetype='text/html')

@babel.localeselector
def get_locale() -> str:
    """ Determine which language is the best match """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == '__main__':
    app.run(debug=True)
