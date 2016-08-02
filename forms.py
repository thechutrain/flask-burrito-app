from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import (DataRequired, Email, Length, EqualTo)


class SignUp(Form):
    email = StringField(
        'Email', validators=[
        DataRequired(),
        Email()
        ])

    password = PasswordField(
    'Password', validators=[
    DataRequired(),
    EqualTo('password2', message="Passwords much match."),
    Length(min=5)
    ])

    password2 = PasswordField('Password2', validators=[])


class Login(Form):
    email = StringField(
        'Email', validators=[
        DataRequired(),
        Email()
        ])
    password = PasswordField(
        'Password', validators=[
        DataRequired()
        ])
