from flask import (Flask, render_template, redirect, url_for, flash)
import json
# from flask_login import (LoginManager, login_user, logout_user,
#                              login_required, current_user)

import forms
import models # where bcrypt is imported


############### Establishing Basics of App ###############
DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)

with open('config.json', 'r') as f:
    config = json.load(f)
app.secret_key = config['flask_app_key']


############### App Pages with Routes ###############
############### Home page
@app.route("/")
def index():
    return "Index page"
    # return render_template("index.html", tacos=taco)

############### Sign UP
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

############### Sign IN
@app.route("/login", methods=("POST", "GET"))
def login():
    form = forms.Login()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash("Your email or password doesn't match!", "error")
            # print("Error")
        else:
            if models.check_password_hash(user.password, form.password.data):
                flash("You have been successfully signed in!", "success")
                # print("Success")
                return redirect(url_for("index"))
            else:
                flash("Your email or password doesn't match!", "error")
                # print("Error")



    return render_template("login.html", form = form)


############### Running Applicaiton ###############
if __name__ == '__main__':
    models.initialize()
    print("models initialized")
    app.run(debug=DEBUG, host=HOST, port=PORT)
