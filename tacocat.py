from flask import (Flask, render_template)
import json

import forms
import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)

# Get passwords from config in .gitignore repo
with open('config.json', 'r') as f:
    config = json.load(f)
app.secret_key = config['flask_app_key']

@app.route("/")
def home_page():
    return render_template("layout.html")

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
