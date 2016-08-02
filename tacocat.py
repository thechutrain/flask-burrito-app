from flask import (Flask, render_template, redirect,
                    url_for, flash, g, request)
import json
from flask_login import (LoginManager, login_user, logout_user,
                             login_required, current_user)

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

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

############### App Pages with Routes ###############
############### Home page
@app.route("/")
def index():
    # return "Index page"
    burritos = models.Burrito.select().limit(5)
    return render_template("index.html", burritos=burritos)
    # return render_template("layout.html")

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
    if current_user.is_authenticated:
        return redirect(url_for("burrito"))
    form = forms.Login()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash("Your email or password doesn't match!", "error")
        else:
            if models.check_password_hash(user.password, form.password.data):
                login_user(user)
                # flash("You have been successfully signed in!", "success")
                flash("Welcome back, {}. You've been successfully signed in.".format(current_user.email),
                "success")
                return redirect(url_for("index"))
            else:
                flash("Your email or password doesn't match!", "error")
    return render_template("login.html", form=form)

############### Sign OUT
@app.route('/logout')
@login_required
def logout():
    # flash("Until next time! Take care, {}".format(current_user.email), "success")
    flash("You've been logged out! Come back soon!", "success")
    logout_user()
    return redirect(url_for('index'))

############### burrito
@app.route("/burrito", methods=("GET", "POST"))
@login_required
def burrito():
    form = forms.Burrito()
    if form.validate_on_submit():
        models.Burrito.create(
            protein = form.protein.data,
            rice = form.rice.data,
            bean = form.rice.data,
            salsa = form.salsa.data,
            sour_cream = form.sour_cream.data,
            cheese = form.cheese.data,
            lettuce = form.lettuce.data,
            extras = form.extras.data,
            # email = g.user._get_current_object().email,
            user = g.user._get_current_object()
        )
        flash("Saved your burrito!", "success")
        return redirect(url_for("index"))
    return render_template("burrito.html", form=form)

############### Running Applicaiton ###############
if __name__ == '__main__':
    models.initialize()
    print("models initialized")
    app.run(debug=DEBUG, host=HOST, port=PORT)
