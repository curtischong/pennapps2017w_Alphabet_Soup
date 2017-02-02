from flask import Flask 
from flask_compress import Compress

app = Flask(__name__) # Create the Flask app 
Compress(app) # Gzip compression for faster load times
app.config['WTF_CSRF_ENABLED'] = False
app.config['SECRET_KEY'] = 'horsebatterystaple'

from app import views # Import views.py at end. Importing at top lines causes import loop error.

