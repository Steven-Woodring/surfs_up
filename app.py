# Dependency
from flask import Flask

# Create Flask app instance
app = Flask(__name__)

# Create Flask routes
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/')
def add_nums():
    return 10+20