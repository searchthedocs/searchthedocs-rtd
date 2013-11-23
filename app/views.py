from functools import wraps
import json

from flask import (
    make_response,
    request,
    Response,
)

from app import app

@app.route('/')
def index():
    return 'searchthedocs demo'

