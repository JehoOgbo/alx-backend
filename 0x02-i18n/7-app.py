#!/usr/bin/env python3
""" Basic flask app
"""
from flask import Flask, render_template, Response, request, g
from flask_babel import Babel # type: ignore
from typing import Dict
import pytz



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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@app.route('/')
def welcome() -> Response:
    return Response(render_template('5-index.html'), mimetype='text/html')

@babel.localeselector
def get_locale() -> str:
    """ Determine which language is the best match """
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])

def get_user() -> Dict:
    """ Returns a user dictionary for login
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None

@babel.timezoneselector
def get_timezone() -> str:
    """ Retrievest the timezone for a web page.
    """
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']

@app.before_request
def before_request() -> None:
    usr = get_user()
    g.user = usr

if __name__ == '__main__':
    app.run(debug=True)
