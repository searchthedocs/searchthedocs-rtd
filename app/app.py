"""
The searchthedocs demo app.
The Flask app is configured here.
"""
import os

from flask import Flask

app = Flask(__name__)

app.config.from_pyfile('config.cfg')
