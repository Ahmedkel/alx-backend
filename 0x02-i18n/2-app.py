#!/usr/bin/env python3
"""Tsk 1: Basic Flask app"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Config class for app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Select and return best language match based on supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    Renders an HTML page
    with a title and a header.
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=True)
