from flask import (Flask, render_template, redirect, url_for, flash)
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
def index():
    return "Index page"
    # return render_template("index.html", tacos=taco)

@app.route("/register", methods=("POST", "GET"))
def register():
    form = forms.SignUp()
    if form.validate_on_submit():
        flash("You're just registered your account", "success")
        models.User.create_user(
            email=form.email.data,
            password=form.password.data
        )
        return redirect(url_for("index"))
    return render_template("register.html", form=form)


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
