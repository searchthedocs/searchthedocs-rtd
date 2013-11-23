"""
Entry-point into the application.
Run with, eg:
gunicorn app.main:app -b 0.0.0.0:8000 --access-logfile -

This loader pattern from:
http://charlesleifer.com/blog/structuring-flask-apps-a-how-to-for-those-coming-from-django/
"""
from app import app
from views import *
